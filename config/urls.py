"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path, re_path

# --
# Add Swagger
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
# --


schema_view = get_schema_view(
    openapi.Info(
        title="Django Rest API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path(r'^admin/$', admin.site.urls),
    # --
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # User Interface App
    path('rest_ui/', include(('rest_ui.urls', 'rest_ui'))),
    # --
    # Django REST Framework (DRF), 
    path('rest_api/', include(('rest_api.urls', 'rest_api'))),
    path('book_rest_api/', include(('book_rest_api.urls', 'book_rest_api'))),
    path('rest_second_api/', include(('rest_second_api.urls', 'rest_second_api'))),
    # --
    # path("prometheus/", include("django_prometheus.urls"))
]


# if settings.DEBUG:
#     urlpatterns += [
#         re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#         re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#         re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
#     ]