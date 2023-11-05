
import requests
from rest_api.injector import URL_HOST
# from .controller.Rule import Rule
import json

# RequestObject = Rule()

class UI_SearchHandler(object):
    
    def __init__(self, logger, RequestObject):
        self.requestobject = RequestObject
        self.logger = logger
        
            
    def Search(self, keyword, pit, direction=None):
        ''' rest_ui search from the template '''
        if not keyword:
            return
        
        # --
        self.logger.warn("UI_SearchHandler: keyword - {}, pit - {} ".format(keyword, pit))
        self.requestobject.get_payload()['query_string'] = keyword
        self.requestobject.get_payload()['pit_id'] = pit
        self.requestobject.get_payload()['direction'] = direction
  
        result = requests.post(url="{}/rest_api/es/search".format(URL_HOST), 
                         data=json.dumps(self.requestobject.get_payload()), 
                         headers=self.requestobject.get_header()
                         )
        # self.logger.info(result.content, type(result.content)) # (<class 'bytes'>,)
        # self.logger.info(json.dumps(result.json(), indent=2))
        # self.logger.info(json.dumps(RequestObject.get_search_result()['hits'], indent=2))
        
        hits, aggs = [], []
        response_results_json = result.json()
        # print(response_results_json)
        # response_results_json = self.requestobject.get_search_result()
        if len(response_results_json['message']['hits']) > 0:
            for hit in response_results_json['message']['hits']:
               hits.append({k.replace("_", '') : v for k, v in hit.items()})
            aggs = [response_results_json['message']['aggregations']]
                
        context = {
            'response': hits,
            'total' : int(response_results_json['message']['total']['value']),
            'keyword': keyword,
            'pit_token' : response_results_json['message']['pit'],
            'aggs' : aggs
        }
        # self.logger.info('UI_SearchHandler Results - {}'.format(json.dumps(context, indent=2)))
        return context