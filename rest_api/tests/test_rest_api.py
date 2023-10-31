
import pytest
import json

# from django.urls import reverse
from ..injector import logger

''' pytest -sv rest_api/tests/test_rest_api.py '''


@pytest.mark.skip(reason="no way of currently testing this")
def test_api_skip():
    assert 1 != 1
    
    
def test_api_test_swagger(mock_client):
    assert mock_client is not None
    
    response = mock_client.get(
        '/rest_api/test'
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Swagger Interface Test"
    }


# `Parametrize` is a builtin mark and one of the killer features of pytest. 
# With this mark, you can perform multiple calls to the same test function.
@pytest.mark.parametrize(
    "obj_id",
    ['1', '2', '3']
)
def test_api_users_swagger(mock_client, obj_id):
    assert mock_client is not None
    
    response = mock_client.get(
        '/rest_api/users?obj_id={}'.format(obj_id)
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Get: hello, world!, value - {}".format(obj_id)
    }
    

def test_api_es_search_swagger(mock_client):
    ''' API call '''
    assert mock_client is not None
    
    request_body = {
        "include_basic_aggs": True,
        "pit_id": "",
        "query_string": "Cryptocurrency",
        "size": 20,
        "sort_order": "DESC",
        "start_date": "2021 01-01 00:00:00"
    }
    response = mock_client.post(
        '/rest_api/es/search',
        data=json.dumps(request_body),
        content_type='application/json',
    )
    assert response.status_code == 200
    results = response.json()
    
    logger.info("results : {}".format(json.dumps(results, indent=2)))
    
    assert results is not None
    assert results['message']['total']['value'] == 2
    
    response_json = results['message']['hits']
    assert response_json[0]['_source']['title'] == "Cryptocurrency Regulations Act 222"
    assert response_json[1]['_source']['title'] == "Cryptocurrency Regulations Act 111"
    
    '''    
    assert results['message']['hits'] == [
      {
        "_index": "test_omnisearch_v1",
        "_id": "222",
        "_score": 0.18232156,
        "_source": {
          "title": "Cryptocurrency Regulations Act 222",
          "locality": "us",
          "bill_type": "BILL",
          "start_date": "2023-01-01 00:00:01"
        },
        "highlight": {
          "title": [
            "<b>Cryptocurrency</b> Regulations Act 222"
          ]
        },
        "sort": [
          0.18232156,
          "Cryptocurrency Regulations Act 222",
          1
        ]
      },
      {
        "_index": "test_omnisearch_v1",
        "_id": "111",
        "_score": 0.18232156,
        "_source": {
          "title": "Cryptocurrency Regulations Act 111",
          "locality": "us",
          "bill_type": "BILL",
          "start_date": "2023-01-01 00:00:00"
        },
        "highlight": {
          "title": [
            "<b>Cryptocurrency</b> Regulations Act 111"
          ]
        },
        "sort": [
          0.18232156,
          "Cryptocurrency Regulations Act 111",
          0
        ]
      }
    ]
    '''
