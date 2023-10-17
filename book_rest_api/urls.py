from django.urls import path, include
from .views import helloAPI

# urlpatterns = [
#     path("", helloAPI, name="home"),
# ]

urlpatterns = [
    path("swagger", helloAPI)
]