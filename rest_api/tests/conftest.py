import pytest
from ..injector import es_client, QueryBuilderInject

# In order to share fixtures across multiple test files, pytest suggests defining fixtures in a conftest.py

@pytest.fixture
def mock_es_client():
    return es_client


@pytest.fixture
def mock_query_builder():
    return QueryBuilderInject

@pytest.fixture
def mock_client():
   from rest_framework.test import APIClient
   return APIClient()

@pytest.fixture
def mock_oas_query():
    oas_query = {
        "include_basic_aggs": True,
        "pit_id": "",
        "query_string": "Cryptocurrency",
        "ids_filter": ["*"],
        "term_filters": [{"fieldname": "genre", "values": ["unknown"]}],
        "size": 20,
        "sort_order": "DESC",
        "start_date": "2021 01-01 00:00:00"
    }
    return oas_query


@pytest.fixture
def userRank_conftest(db):
    """
    Create a test user.
    """
    from ..models import userRank
    created = userRank.objects.create(username='john', deposit=11, earning_rate=11)
    return created