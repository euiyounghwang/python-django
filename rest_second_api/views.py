

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, permissions, generics, status

from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING, TYPE_ARRAY
from drf_yasg.utils import swagger_auto_schema

from django.http.response import JsonResponse
from rest_framework.response import Response

# Create your views here.
class TestView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['Sample'], 
                         operation_summary="Swagger GET Test", 
                         metheod=['GET'], 
                         responses={200: Schema(type=TYPE_OBJECT)}
    )
    def get(self, request):
        return Response({'message' : 'Swagger Interface Test'})