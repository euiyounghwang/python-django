
import requests
from rest_api.injector import URL_HOST
# from .controller.Rule import Rule
import json

# RequestObject = Rule()

class UI_SearchHandler(object):
    
    def __init__(self, logger, RequestObject):
        self.requestobject = RequestObject
        self.logger = logger
    
    def Search(self, keyword):
        # --
        self.requestobject.get_payload()['query_string'] = keyword
  
        result = requests.post(url="{}/rest_api/es/search".format(URL_HOST), 
                         data=json.dumps(self.requestobject.get_payload()), 
                         headers=self.requestobject.get_header()
                         )
        # self.logger.info(result.content, type(result.content)) # (<class 'bytes'>,)
        self.logger.info(json.dumps(result.json(), indent=2))
        # self.logger.info(json.dumps(RequestObject.get_search_result()['hits'], indent=2))
        
        hits = []
        # response_results_json = result.json()
        response_results_json = self.requestobject.get_search_result()
        for hit in response_results_json['hits']:
            each_dict = hit
            # print(hit)
            if '_source' in each_dict: 
                each_dict.update({"source" : hit['_source']})
                del each_dict['_source']
            hits.append(each_dict)
            
        context = {
            'response': hits,
            'total' : int(response_results_json['total']['value']),
            'keyword': keyword
        }
        # self.logger.info('UI_SearchHandler Results - {}'.format(json.dumps(context, indent=2)))
        return context