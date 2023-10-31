
import pytest
import json
# from ..injector import QueryBuilderInject


@pytest.mark.skip(reason="no way of currently testing this")
def test_build_skip():
    assert 1 != 1


@pytest.mark.parametrize(
    "_term",
    [[1, 2, 3, 4, 5, 6]]
)
def test_build_terms(mock_query_builder, _term):
    ''' terms query build test '''
    assert mock_query_builder is not None
    mock_query_handler = mock_query_builder
    
    mock_ids_filter = _term
    
    response_ids_filter_query = mock_query_handler.build_terms_filters_batch(_terms=mock_ids_filter, max_terms_count=5)
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

    response_ids_filter_query = mock_query_handler.build_terms_filters_batch(_terms=mock_ids_filter, max_terms_count=1)
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
