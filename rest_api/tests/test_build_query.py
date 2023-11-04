
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
    
    expected_query_string = mock_query_handler.transform_query_string(payload)
    assert expected_query_string == {
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
    assert json_value_to_transform_trim(expected_query_string) == {
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
    expected_search_after_clause = mock_query_builder.add_pagination(search_after=sort_values)
    assert expected_search_after_clause == sort_values


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

    expected_ids_filter_query = mock_query_handler.build_terms_filters_batch(
        fieldname="_id", _terms=mock_ids_filter, max_terms_count=5)
    assert expected_ids_filter_query is not None
    assert expected_ids_filter_query == [
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

    expected_ids_filter_query = mock_query_handler.build_terms_filters_batch(
       fieldname="_id", _terms=mock_ids_filter, max_terms_count=1)
    assert expected_ids_filter_query is not None
    assert expected_ids_filter_query == [
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

    expected_ids_filter_query = mock_query_handler.build_terms_filters_batch(
        fieldname="_id", _terms=mock_ids_filter, max_terms_count=5)
    assert expected_ids_filter_query is not None
    assert expected_ids_filter_query == [
        {
            "terms": {
                "_id": [
                    "111",
                    "222"
                ]
            }
        }
    ]
    

def test_build_terms_filter(mock_query_builder, mock_oas_query):
    ''' terms query build test '''
    ''' pytest -sv rest_api/tests/test_build_query.py::test_build_terms_filter '''
    assert mock_query_builder is not None
    assert mock_oas_query is not None
    
    mock_query_handler = mock_query_builder
    # --
    # op : 'must'
    # --
    expected_term_filters = mock_query_handler.build_term_filter(mock_oas_query.get("term_filters"), 'must')
    print("\nexpected_term_filters 'must' - {}".format(json.dumps(expected_term_filters, indent=2)))
    assert expected_term_filters == {
        "bool": {
            "must": [
                {
                    "bool": {
                        "filter": {
                            "terms": {
                                "genre": [
                                    "unknown"
                            ]
                            }
                        }
                    }
                }
            ]
        }
    }
    
    # --
    # op : 'should'
    # --
    expected_term_filters = mock_query_handler.build_term_filter(mock_oas_query.get("term_filters"), 'should')
    print("\nexpected_term_filters 'should' - {}".format(json.dumps(expected_term_filters, indent=2)))
    assert expected_term_filters == {
        "bool": {
            "should": [
                {
                    "bool": {
                        "filter": {
                            "terms": {
                                "genre": [
                                    "unknown"
                                ]
                            }
                        }
                    }
                }
            ]
        }
    }
    
    # --
    # op : 'not'
    # --
    mock_oas_query.update({
        'term_filters' : [
            {
                "not": [
                    {
                        'fieldname': 'genre',
                        'values': ['unknown']
                    }
                ]
            }
        ]
    })
    expected_term_filters = mock_query_handler.build_term_filter(mock_oas_query.get("term_filters"), 'must')
    print("\nexpected_term_filters 'not' - {}".format(json.dumps(expected_term_filters, indent=2)))
    assert expected_term_filters == {
        "bool": {
            "must": [
                {
                    "bool": {
                        "must_not": [
                            {
                                "bool": {
                                    "filter": {
                                        "terms": {
                                            "genre": [
                                                "unknown"
                                            ]
                                        }
                                    }
                                }
                             }
                        ]
                    }
                }
            ]
        }
    }
    
    # --
    # op : 'not' and 'AND'
    # --
    mock_oas_query.update({
        'term_filters' : [
            {
                "not": [
                    {
                        'fieldname': 'genre',
                        'values': ['unknown']
                    },
                    {
                        "or": [
                            {
                                'fieldname': 'genre',
                                'values': ['unknown']
                            },
                            {
                                'fieldname': 'genre',
                                'values': ['unknown1']
                            }
                        ]
                    }
                ]
            }
        ]
    })
    expected_term_filters = mock_query_handler.build_term_filter(mock_oas_query.get("term_filters"), 'must')
    print("\nexpected_term_filters 'not' and 'AND' - {}".format(json.dumps(expected_term_filters, indent=2)))
    assert expected_term_filters == {
        "bool": {
            "must": [
            {
                "bool": {
                "must_not": [
                    {
                        "bool": {
                            "filter": {
                                "terms": {
                                    "genre": [
                                    "unknown"
                                    ]
                                }
                            }
                        }
                    },
                    {
                        "bool": {
                            "should": [
                            {
                                "bool": {
                                    "filter": {
                                        "terms": {
                                        "genre": [
                                            "unknown"
                                        ]
                                        }
                                    }
                                }
                            },
                            {
                                "bool": {
                                    "filter": {
                                        "terms": {
                                        "genre": [
                                            "unknown1"
                                        ]
                                        }
                                    }
                                }
                            }
                            ]
                        }
                    }
                ]
                }
            }
            ]
        }
    }
        
    # --
    # op : 'or'
    # --
    mock_oas_query.update({
        'term_filters' : [
            {
                "or": [
                    {
                        'fieldname': 'genre',
                        'values': ['unknown']
                    },
                     {
                        'fieldname': 'genre',
                        'values': ['unknown1']
                    }
                ]
            }
        ]
    })
    expected_term_filters = mock_query_handler.build_term_filter(mock_oas_query.get("term_filters"), 'must')
    print("\nexpected_term_filters 'or' - {}".format(json.dumps(expected_term_filters, indent=2)))
    assert expected_term_filters == {
        "bool": {
            "must": [
                {
                    "bool": {
                        "should": [
                            {
                                "bool": {
                                    "filter": {
                                        "terms": {
                                            "genre": [
                                                "unknown"
                                            ]
                                        }
                                    }
                                }
                             },
                            {
                                "bool": {
                                    "filter": {
                                        "terms": {
                                            "genre": [
                                                "unknown1"
                                            ]
                                        }
                                    }
                                }
                             }
                        ]
                    }
                }
            ]
        }
    }
    
    # --
    # op : 'must' with multiple term_filters
    # --
    mock_oas_query.update({'term_filters' : [
        {"fieldname": "genre", "values": ["unknown"]},
        {"fieldname": "film", "values": ["sports"]},
    ]})
    expected_term_filters = mock_query_handler.build_term_filter(mock_oas_query.get("term_filters"), 'must')
    print("\nexpected_term_filters 'must' with multiple filters - {}".format(json.dumps(expected_term_filters, indent=2)))
    assert expected_term_filters == {
        "bool": {
            "must": [
                {
                    "bool": {
                        "filter": {
                            "terms": {
                                "genre": [
                                    "unknown"
                                ]
                            }
                        }
                    }
                },
                {
                    "bool": {
                        "filter": {
                            "terms": {
                                "film": [
                                    "sports"
                                ]
                            }
                        }
                    }
                }
            ]
        }
    }
