
import json
from elasticsearch import TransportError
import elasticsearch.exceptions


class SearchOmniHandler(object):
    
    def __init__(self, es_client, logger):
        self.es_client = es_client
        self.logger = logger
        self.OMNI_INDEX_ALIAS = 'omnisearch_search'
        self.search_after = None
        
        # --
        # Test ES connection
        self.es_live_validation()
        
        
    def es_live_validation(self):
        '''
        es_client test
        '''
        self.logger.info(json.dumps(self.es_client.info(), indent=2))
    
    
    def search(self, query_build, oas_query=None):
        if not oas_query:
            oas_query = {}
        self.logger.info("oas_query : {}".format(oas_query))
        
        if not oas_query.get('pit_id'):
            self.logger.warn("Search but It's first time to call with pit")
            resp = self.es_client.open_point_in_time(index=self.OMNI_INDEX_ALIAS, keep_alive='1m')
            pit_id = resp['id']
            self.search_after = None
        else:
            pit_id = oas_query.get('pit_id')
        
        es_query = query_build.build_query(oas_query, pit_id, self.search_after)
        self.logger.info('query_builder_build_query:oas_query - {}'.format(json.dumps(es_query, indent=2)))

        try:
            es_result = self.es_client.search(
                body=es_query,
            )
        # This is what Elasticserch throws as an exception if the point in time context has expired
        except elasticsearch.exceptions.NotFoundError as nfe:
            raise ContinuationTokenException(
                "Continuation token has expired. Please set the token to None/null and restart the pagination.")

        # self.logger.info('query_builder_build_query:response - {}'.format(json.dumps(es_result, indent=2)))
        es_hits = es_result["hits"]
        results = [es_hit for es_hit in es_hits["hits"]]

        if results:
            if oas_query.get('direction') == 'right':
                self.search_after = results[int(len(results))-1]["sort"]
                self.logger.warn("Paging to Right - {}".format(len(results)))
            else:
                self.search_after = results[0]["sort"]
                self.logger.warn("Paging to Left")
                    
        es_hits['pit'] = pit_id
        es_hits['aggregations'] = es_result['aggregations']

        return es_hits
    