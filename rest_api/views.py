from django.shortcuts import render

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .config.log_config import create_log
import json

from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING, TYPE_ARRAY
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


logger = create_log()


# Create your views here.
class TestView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['my custom tag'])
    def get(self, request):
        return Response("Swagger 연동 테스트")


class RestapiView(APIView):
    permission_classes = [permissions.AllowAny]
    
    @swagger_auto_schema(tags=['rest_api'], responses={200: Schema(type=TYPE_OBJECT)})
    def get(self, request):
        logger.info('request helloAPI')
        return Response({'message' : 'Get: hello, world!'})
    
    # @swagger_auto_schema(tags=['rest_api'], method='post', request_body=login_schema, responses={200: Schema(type=TYPE_OBJECT)})
    @swagger_auto_schema(tags=['rest_api'], responses={
    status.HTTP_200_OK: Schema(
        type=TYPE_OBJECT,
        properties={
        #    'students': Schema(
        #       type=TYPE_ARRAY
        #    )
            "message": "hello, world!"
        }
       )
    })
    def post(self, request):
        tutorial_data = JSONParser().parse(request)
        # print('request : {}'.format(json.dumps(tutorial_data, indent=2)))
        logger.info('request : {}'.format(json.dumps(tutorial_data, indent=2)))
        return JsonResponse({'message' : 'Post: hello, world!'})

    '''
    @api_view(['GET', 'POST'])
    @swagger_auto_schema(tags=['rest_api'])
    def helloAPI(self, request):
        if request.method == 'GET':
            # return Response("hello, world!")
            logger.info('request helloAPI')
            return Response({'message' : 'Get: hello, world!'})
        
        elif request.method == 'POST':
            tutorial_data = JSONParser().parse(request)
            # print('request : {}'.format(json.dumps(tutorial_data, indent=2)))
            logger.info('request : {}'.format(json.dumps(tutorial_data, indent=2)))
            return JsonResponse({'message' : 'Post: hello, world!'})
    '''
