from django.urls import path, include, re_path
from django.contrib import admin

# --
# Add Swagger
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from django.conf import settings
from drf_yasg import openapi
from rest_framework import permissions

from .views import (
    StudentViewSet, userRankViewSet, SearchView
)

from .views_test import (
    RestapiView, TestView,
    get_student_date_joined, get_note, get_note_joined
)

# from .models import Student, userRank

# Register your models here.
# admin.site.register(Student)

# --
# Model && Serializer
# Create Model api automatically [GET, POST, PUT, DELETE]
from .router import router
 # --

urlpatterns = [

    path('test', TestView.as_view(), name='test1'),
    
    # path('Note', get_note, name='Note'),
    # path('Note/<int:pk>', get_note_joined, name='Note'),
    # path('Note', get_note_post_joined, name='Note'),
    
    # --
    # es search
    path('es/search', SearchView.get_es_search, name='Search'),
    # --
    
    # --
    # Model && Serializer
    # https://pjs21s.github.io/vuejs-restframe/
    path('', include(router.urls)),
    # --
    
    path('users', RestapiView.as_view(), name='rest_api'),
    # path('users/<str:obj_id>', RestapiView.as_view(), name='rest_api'),
    
    # path('student-date-joined/<int:pk>', get_student_date_joined, name='get-student-date-joined'), # new line
    # http://localhost:9999/rest_api/prometheus/metrics
    path("prometheus/", include("django_prometheus.urls"))
]

# router = DefaultRouter()
# router.register('data', helloAPI, basename='data')
# urlpatterns = router.urls
