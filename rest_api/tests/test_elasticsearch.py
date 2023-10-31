
import pytest
from elasticsearch.client import Elasticsearch, IndicesClient
from ..service.Utils.ES_Utils import transform_trim_string
import json

''' pytest -sv rest_api/tests/test_elasticsearch.py '''

@pytest.mark.skip(reason="no way of currently testing this")
def test_search_skip():
    assert 1 != 1
    

# @pytest.fixture(scope="session")
def test_elasticsearch(mock_es_client):
    # ES 7 will be on 9200 and setup basic index with some datas into local elasticsearch cluster
    assert mock_es_client is not None

    es = mock_es_client

    # ic = IndicesClient(mock_es_client)
    # IndicesClient is equal to es.indices
    ic = es.indices

    def try_delete_index(index):
        try:
            if ic.exists(index):
                # print('Delete index : {}'.format(index))
                ic.delete(index)
        except NotFoundError:
            pass
    try_delete_index("test_ngram_v1")
    try_delete_index("test_performance_metrics_v1")
    try_delete_index("test_service_realtime_metrics_v1")

    def create_index(index, def_file_name):
        from os.path import dirname
        # print(open(dirname(__file__) + def_file_name))
        with open(dirname(__file__) + def_file_name) as f:
            index_def = f.read()
        ic.create(index, index_def)
    create_index("test_ngram_v1", "/test_mapping/omnisearch_ngram_mapping.json")
    create_index("test_performance_metrics_v1", "/test_mapping/performance_metrics_mapping.json")
    create_index("test_service_realtime_metrics_v1", "/test_mapping/performance_metrics_mapping.json")

    # ngram index
    es.index(index="test_ngram_v1", id=111, body={
            "title": " The quick brown fox jumps over the lazy dog"
        }
    )

    # refresh
    es.indices.refresh(index="test_ngram_v1")


def test_indics_analyzer_elasticsearch(mock_es_client):
    assert mock_es_client is not None

    es = mock_es_client
    ic = es.indices
    response = ic.analyze(
        index="test_ngram_v1",
        body={
            "analyzer": "autocomplete",
            "text": transform_trim_string("The quick"),
        }
    )
    
    assert response is not None
    # the should be stopword
    assert response == {
        "tokens":[
            {
                "token":"th",
                "start_offset":0,
                "end_offset":2,
                "type":"word",
                "position":0
            },
            {
                "token":"qu",
                "start_offset":4,
                "end_offset":6,
                "type":"word",
                "position":2
            },
            {
                "token":"qui",
                "start_offset":4,
                "end_offset":7,
                "type":"word",
                "position":3
            },
            {
                "token":"quic",
                "start_offset":4,
                "end_offset":8,
                "type":"word",
                "position":4
            },
            {
                "token":"quick",
                "start_offset":4,
                "end_offset":9,
                "type":"word",
                "position":5
            }
        ]
    }

 