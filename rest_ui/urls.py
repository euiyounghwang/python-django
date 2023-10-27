from django.urls import path
from .views import rest_apis, rest_search_apis, rest_search_main

urlpatterns = [
    # --
    # Render Template using HTTPResponse to the browser)
    #  path('', rest_apis, name='rest_ui'),
    path('', rest_search_main, name='rest_ui'),
    path('search', rest_search_apis, name='rest_ui'),
    # --
    
]