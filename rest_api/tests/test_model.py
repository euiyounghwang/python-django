
import pytest
from django.urls import reverse


''' pytest -sv rest_api/tests/test_model.py '''


# @pytest.mark.django_db
# def test_unauthorized_request(mock_client):
#    url = reverse('userRank')
#    response = mock_client.get(url)
#    assert response.status_code == 200


from ..models import Student, userRank
# from django.contrib.models import Student, userRank

# @pytest.mark.django_db
# def test_student_create(db):
# #    created = Student.objects.create(name='john', grade=10, age=11, home_address='addr..')
#    created = userRank.objects.create(username='john', deposit=11, earning_rate=11)
#    assert created is not None
# #    assert created.username == 'john'
