from django.urls import path, include, re_path
from .views import RestapiView, TestView

from django.contrib import admin

# --
# Add Swagger
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from django.conf import settings
from drf_yasg import openapi
from rest_framework import permissions
# --

# from rest_framework.routers import DefaultRouter

# app_name='blog'
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    # path("swagger", helloAPI),
    # path('docs/', TestView.as_view(), name='test'),
    path('test', TestView.as_view(), name='test1'),
    path('sample', RestapiView.as_view(), name='rest_api'),
    # http://localhost:9999/rest_api/prometheus/metrics
    path("prometheus/", include("django_prometheus.urls"))
]

# router = DefaultRouter()
# router.register('data', helloAPI, basename='data')
# urlpatterns = router.urls
