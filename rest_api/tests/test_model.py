
import pytest
from django.urls import reverse
from django.test import Client
from ..models import userRank
import json

''' pytest -sv rest_api/tests/test_model.py '''

def test_django_test_request(mock_client):
   client = Client ()
   response = client.get('/rest_api/test')
   print(json.dumps(response.json(), indent=2))
   assert response.status_code == 200
   assert response.json() == {
    "message": "Swagger Interface Test"
   }


@pytest.mark.django_db
def test_django_test_request(mock_client):
   ''' reverse(app_name:name for url) '''
#    reverse("item-detail", args=[item_id])
   url = reverse('rest_api_app:test_api')
   response = mock_client.get(url)
   print(json.dumps(response.json(), indent=2))
   assert response.status_code == 200
   assert response.json() == {
    "message": "Swagger Interface Test"
   }


@pytest.mark.django_db(transaction=True)
def test_transaction_true_db_fixture(userRank_conftest):
    assert True
    

@pytest.mark.django_db
def test_userRank_create():
#    created = Student.objects.create(name='john', grade=10, age=11, home_address='addr..')
   """
   Create a test user.
   """
   created = userRank.objects.create(username='euiyoung', deposit=999, earning_rate=999)
   assert created is not None
   get_row = userRank.objects.get(username='euiyoung')
   assert get_row is not None
   assert get_row.json() == {
       'deposit': 999, 'earning_rate': 999.0, 'username': 'euiyoung'
   }
   created = userRank.objects.create(username='hwang', deposit=999, earning_rate=999)
   assert created is not None
   get_row = userRank.objects.get(username='hwang')
   assert get_row is not None
   assert get_row.json() == {
       'deposit': 999, 'earning_rate': 999.0, 'username': 'hwang'
   }
   assert userRank.objects.count() == 2
   print(userRank)
   

   

