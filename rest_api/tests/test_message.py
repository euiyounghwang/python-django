import pytest
import unittest
import uuid
# import asyncio
from ..injector import Redis_Cache

''' pytest -sv rest_api/tests/test_message.py::TestMessageuilders::test_redis_assign_test '''

class TestMessageuilders(unittest.TestCase):


    def test_redis_client(self):
        MockRedisInsHandler = Redis_Cache
        assert MockRedisInsHandler is not None
        
    def test_redis_assign_test(self):
        MockRedisInsHandler = Redis_Cache
        assert MockRedisInsHandler is not None
        
        UUID = str(uuid.uuid4())
        MockRedisInsHandler.set_json_key(UUID, 'test')
        # print(RedisCacheHandlers.get_transformed_dict('1234')[0])
        response_json = MockRedisInsHandler.get_transformed_dict(UUID)[0]
        
        exclue_columns = ['INPUT_DATE', 'EXPIRED_SECONDS']
        for column in exclue_columns:
            del response_json[column]
            
        # print(type(response_json))
        print(response_json)
        assert response_json == {
            "KEY": UUID, 
            "REQUEST_USER_ID": "pd292816", 
            "OBJECT_V": 'test'
        }
        
        assert MockRedisInsHandler.delete_key(UUID) is not None