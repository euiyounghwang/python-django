import pytest
from ..injector import es_client

# In order to share fixtures across multiple test files, pytest suggests defining fixtures in a conftest.py

@pytest.fixture
def mock_es_client():
    return es_client

