
import pytest
from django.urls import reverse
from django.test import Client
from ..models import userRank, Student
import json

''' pytest -sv rest_api/tests/test_model.py '''

def test_django_test_request():
   client = Client ()
   response = client.get('/rest_api/test')
   print(json.dumps(response.json(), indent=2))
   assert response.status_code == 200
   assert response.json() == {
    "message": "Swagger Interface Test"
   }


@pytest.mark.django_db
# To gain access to the database pytest-django get django_db mark or request one of the db, transactional_db 
def test_django_reverse_test_request(mock_client):
   ''' reverse(app_name:name for url) '''
#    reverse("item-detail", args=[item_id])
   url = reverse('rest_api_app:test_api')
   response = mock_client.get(url)
   print(json.dumps(response.json(), indent=2))
   assert response.status_code == 200
   assert response.json() == {
    "message": "Swagger Interface Test"
   }
   

@pytest.mark.django_db
def test_django_reverse_users_request(mock_client):
   ''' reverse(app_name:name for url) '''
#    reverse("item-detail", args=[item_id])
   url = reverse('rest_api_app:users')
   response = mock_client.get(url)
   print(json.dumps(response.json(), indent=2))
   assert response.status_code == 200
   print(response)
   assert response.json() == {
      "message": "Get: hello, world!, value - None"
   }
   
   from django.shortcuts import resolve_url
   # --
   # with arguments
   obj_id = 1
   # url = reverse('rest_api_app:users', kwargs={'object_id' : 1})
   url = resolve_url('rest_api_app:users')
   print(url)
   response = mock_client.get(url + "?obj_id={}".format(obj_id))
   assert response.status_code == 200
   print(response)
   assert response.json() == {
      "message": "Get: hello, world!, value - 1"
   }


@pytest.mark.django_db
@pytest.mark.parametrize(
   'obj_id',
   ['Yasou', 'Guten tag','Bonjour']
)
def test_reverse_model_parametrize(mock_client, obj_id):
   url = reverse('rest_api_app:users')
   response = mock_client.get(
       url, data={'obj_id': obj_id}
   )
   assert response.status_code == 200
   assert response.json() == {
      "message": "Get: hello, world!, value - {}".format(obj_id)
   }


@pytest.mark.django_db(transaction=True)
def test_transaction_true_db_fixture(userRank_conftest):
    assert True
    

@pytest.mark.django_db
def test_student_create():
   """
   Create a test user.
   """
   created = Student.objects.create(name='john', grade=10, age=11, home_address='addr..', gender='Male')
   assert created is not None
   get_row = Student.objects.get(name='john')
   assert get_row is not None
   assert get_row.json() == {
       'name':'john', 'grade' : 10, 'age' : 11, 'home_address' : 'addr..', 'gender' : 'Male'
   }
   assert Student.objects.count() == 1



@pytest.mark.django_db
def test_userRank_create():
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
   

   

