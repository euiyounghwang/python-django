from django.urls import path
from .views import rest_apis

urlpatterns = [
    # --
    # Render Template using HTTPResponse to the browser)
     path('', rest_apis, name='rest_ui'),
    # --
    
]