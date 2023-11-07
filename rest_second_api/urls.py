
from django.urls import path, include, re_path
from django.contrib import admin

from .views import (
    TestView
)

app_name = 'rest_second_api_app'
urlpatterns = [
    path('test', TestView.as_view(), name='test_api'),
]