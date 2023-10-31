
import pytest
import json
# from ..injector import QueryBuilderInject
from ..service.Utils.ES_Utils import json_value_to_transform_trim


''' pytest -sv rest_api/tests/test_build_query.py '''
''' pytest -sv rest_api/tests/test_build_query.py::test_transform_trim '''


@pytest.mark.skip(reason="no way of currently testing this")
def test_build_skip():
    assert 1 != 1


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
        _terms=mock_ids_filter, max_terms_count=5)
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
        _terms=mock_ids_filter, max_terms_count=1)
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
        _terms=mock_ids_filter, max_terms_count=5)
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
