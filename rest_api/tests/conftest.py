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