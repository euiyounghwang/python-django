
import pytest
import json
# from ..injector import QueryBuilderInject
from ..service.Utils.ES_Utils import json_value_to_transform_trim


''' pytest -sv rest_api/tests/test_build_query.py '''
''' pytest -sv rest_api/tests/test_build_query.py::test_transform_trim '''


@pytest.mark.skip(reason="no way of currently testing this")
def test_build_skip():
    assert 1 != 1


def test_query_string_clause(mock_query_builder):
    ''' query_string build '''
    assert mock_query_builder is not None
    mock_query_handler = mock_query_builder
    
    payload = {
        "include_basic_aggs": True,
        "pit_id": "",
        "query_string": "Cryptocurrency ",
        "ids_filter" : ["*"],
        "size": 20,
        "sort_order": "DESC",
        "start_date": "2021 01-01 00:00:00"
    }
    
    query_string_clause = mock_query_handler.transform_query_string(payload)
    assert query_string_clause == {
        "query_string": {
            "fields": [
              "*"
            ],
            "default_operator": "AND",
            "analyzer": "standard",
            "query": "Cryptocurrency "
          }
    }
    
    # --
    # trim all values in json
    # --
    assert json_value_to_transform_trim(query_string_clause) == {
        "query_string": {
            "fields": [
              "*"
            ],
            "default_operator": "AND",
            "analyzer": "standard",
            "query": "Cryptocurrency"
          }
    }


def test_pagination_clause(mock_query_builder):
    ''' search_after with pit build '''
    assert mock_query_builder is not None
    mock_query_handler = mock_query_builder
    
    search_after_clause = mock_query_builder.add_pagination(search_after=None)
    assert search_after_clause == None
    
    # --
    # Paging with pit
    sort_values = [5.5595245, "Jai Prakash", 4294970921]
    search_after_clause = mock_query_builder.add_pagination(search_after=sort_values)
    assert search_after_clause == sort_values


def test_transform_trim():
    test_query = {
        "query": {
            "bool": {
                "must": [
                    {
                        "query_string": {
                            "fields": [
                                "*"
                            ],
                            "default_operator": "AND",
                            "analyzer": "    standard ",
                            "query": " video "
                        }
                    }
                ]
            }
        }
    }
    assert json_value_to_transform_trim(test_query) is not None
    assert json_value_to_transform_trim(test_query) == {
        "query": {
            "bool": {
                "must": [
                    {
                        "query_string": {
                            "fields": [
                                "*"
                            ],
                            "default_operator": "AND",
                            "analyzer": "standard",
                            "query": "video"
                        }
                    }
                ]
            }
        }
    }


# `Parametrize` is a builtin mark and one of the killer features of pytest.
# With this mark, you can perform multiple calls to the same test function.
@pytest.mark.parametrize(
    "_term",
    [[1, 2, 3, 4, 5, 6]]
)
def test_build_terms(mock_query_builder, _term):
    ''' terms query build test '''
    assert mock_query_builder is not None
    mock_query_handler = mock_query_builder

    mock_ids_filter = _term

    response_ids_filter_query = mock_query_handler.build_terms_filters_batch(
        field="_id", _terms=mock_ids_filter, max_terms_count=5)
    assert response_ids_filter_query is not None
    assert response_ids_filter_query == [
        {
            "terms": {
                "_id": [
                    1,
                    2,
                    3,
                    4,
                    5
                ]
            }
        },
        {
            "terms": {
                "_id": [
                    6
                ]
            }
        }
    ]


def test_build_terms_batch(mock_query_builder):
    ''' terms query build test '''
    assert mock_query_builder is not None
    mock_query_handler = mock_query_builder

    mock_ids_filter = [
        "111", '222'
    ]

    response_ids_filter_query = mock_query_handler.build_terms_filters_batch(
       field="_id", _terms=mock_ids_filter, max_terms_count=1)
    assert response_ids_filter_query is not None
    assert response_ids_filter_query == [
        {
            "terms": {
                "_id": [
                    "111"
                ]
            }
        },
        {
            "terms": {
                "_id": [
                    "222"
                ]
            }
        }
    ]

    response_ids_filter_query = mock_query_handler.build_terms_filters_batch(
        field="_id", _terms=mock_ids_filter, max_terms_count=5)
    assert response_ids_filter_query is not None
    assert response_ids_filter_query == [
        {
            "terms": {
                "_id": [
                    "111",
                    "222"
                ]
            }
        }
    ]
