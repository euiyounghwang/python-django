from django.shortcuts import render

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .config.log_config import create_log
import json


logger = create_log()

# Create your views here.
@api_view(['GET', 'POST'])
def helloAPI(request):
    if request.method == 'GET':
        # return Response("hello, world!")
        logger.info('request helloAPI')
        return Response({'message' : 'Get: hello, world!'})
    
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        # print('request : {}'.format(json.dumps(tutorial_data, indent=2)))
        logger.info('request : {}'.format(json.dumps(tutorial_data, indent=2)))
        return JsonResponse({'message' : 'Post: hello, world!'})
