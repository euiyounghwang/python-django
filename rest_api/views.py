from django.shortcuts import render

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response

from rest_framework.views import APIView
from django.views import View

from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .config.log_config import create_log
import json

from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING, TYPE_ARRAY
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Student, userRank
from .serializers import StudentSerializer, userRankSerializer

# --
# Service
# from .service.Handler.SearchOmniHandler import SearchOmniHandler
from .injector import SearchOmniHandlerInject, QueryBuilderInject, logger


# logger = create_log()
# SearchOmniObject = SearchOmniHandler(logger=logger)

# --
# Class Based View for Create, Read, Update, Delete
# Increased productivity, readability
# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class userRankViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """
    queryset = userRank.objects.all()
    serializer_class = userRankSerializer



class RedisView(APIView):
    permission_classes = [permissions.AllowAny]
    
    @swagger_auto_schema(tags=['Redis'], operation_summary="Redis Health GET", method='GET', responses={200: Schema(type=TYPE_OBJECT)})
    @api_view(["GET",])
    def get_redis_health(request):
        try:
            logger.info("ES get_redis_health")
            from django_redis import get_redis_connection
            logger.info("Redis Connection : {}".format(get_redis_connection("default").flushall()))
            return Response({'message' : 'Get: Redis Connection - {}'.format(get_redis_connection("default").flushall())})
        except Exception as e:
            logger.error(e)
            
    
    @swagger_auto_schema(tags=['Redis'], operation_summary="Redis GET", method='GET', responses={200: Schema(type=TYPE_OBJECT)})
    @api_view(["GET",])
    def get_redis_search(request):
        try:
            logger.info("ES get_redis_search")
            from django_redis import get_redis_connection
            print(get_redis_connection("default").flushall())
            return Response({'message' : 'Get: hello, get_redus_search world!'})
        except Exception as e:
            logger.error(e)



class SearchView(APIView):
    permission_classes = [permissions.AllowAny]
 
    @swagger_auto_schema(
        tags=["Search"],
        methods=['POST'],
        operation_summary="Search to ES",
        request_body = openapi.Schema(
        title= "Create Dataset",
        type=openapi.TYPE_OBJECT, 
        properties={
            'include_basic_aggs': openapi.Schema(type=TYPE_STRING, description='boolean', example="true"),
            'pit_id': openapi.Schema(type=openapi.TYPE_STRING, description='pit_id', example=""),
            'query_string': openapi.Schema(type=openapi.TYPE_STRING, description='query_string', example="video"),
            'size': openapi.Schema(type=openapi.TYPE_INTEGER, description='size', example=20),
            'sort_order': openapi.Schema(type=openapi.TYPE_STRING, description='sort_order', example="DESC"),
            # 'start_date': openapi.Schema(type=openapi.TYPE_STRING, description='start_date', example="2022-05-27T12:48:07.256Z", format="YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]"),
            'start_date': openapi.Schema(type=openapi.TYPE_STRING, description='start_date', example="2021 01-01 00:00:00", format="YYYY-MM-DD HH:MM:ss"),
        }),
        # responses={200: Schema(type=TYPE_OBJECT)})
        responses={
            200: 'Search results was returned..',
            404: 'Search results was not returned..',
            500: 'Server has an error..',
        }
        # responses={200: openapi.Schema(type=openapi.TYPE_INTEGER,title="s")}
        )
    @api_view(['POST'])
    def get_es_search(request):
        try:
            # print(request.data)
            request_json = request.data
            # tutorial_data = JSONParser().parse(request)
            # print('request : {}'.format(json.dumps(request_json, indent=2)))
            logger.info('get_es_search : {}'.format(json.dumps(request_json, indent=2)))
            response = SearchOmniHandlerInject.search(QueryBuilderInject, request_json)
            return JsonResponse({'message' : response}, status=200)
        except Exception as e:
            logger.error(e)
            return JsonResponse({'message' : str(e)}, status=500)
            
            
    @api_view(["GET",])
    def get_search(request):
        try:
            logger.info("ES get_search")
            return Response({'message' : 'Get: hello, search world!'})
        except Exception as e:
            logger.error(e)
                
            
            
# --
# REST API : CRUD Custom URL Patterns to this class
# https://walkingplow.tistory.com/25
class userRankView(APIView):
    """
    Custom REST API GET, PUT, DELETE, POST
    """

    @swagger_auto_schema(tags=['userank'], operation_summary="userank GET", method='GET', responses={200: Schema(type=TYPE_OBJECT)})
    @api_view(["GET",])
    def get_api(request, pk=None):
        """using this api for get with {id} && get_all"""
        logger.info('request : {}'.format(request))
        
        # human = Human.objects.get(dog__id = dog.id)
        userRanks = userRank.objects.all() if pk is None else userRank.objects.filter(username=pk).all()
                    
        logger.info("userRanks : {}".format(userRanks))
        userRanksList = []
        for userRankItem in userRanks:
            userRanksList.append(
                {
                        "username": userRankItem.username,
                        "deposit": userRankItem.deposit,
                        "earning_rate": userRankItem.earning_rate,
                }
            )

        return JsonResponse({"results": userRanksList}, status=200)
        
    
    
    @swagger_auto_schema(tags=['userank'], operation_summary="userank DELETE with Params", method='DELETE', responses={200: Schema(type=TYPE_OBJECT)})
    @api_view(["DELETE",])
    def delete_params_api(request, username=None):
        """using this api for delete with {id}"""
        if username is None:
            # logger.info("userRanks : {}".format(userRanks))
            return JsonResponse({"results": userRanksList}, status=200)
        logger.info('request : {}'.format(request))
        logger.info('username : {}'.format(username))
        # student = get_object_or_404(Student, pk=pk)
        userRanks = userRank.objects.filter(username=username).all()
        if userRanks:
            logger.info('Item was existing : {}'.format(username))
            userRanks.delete()
            return JsonResponse({"results": 'Item was deleted'}, status=200)
        return JsonResponse({"results": 'Item was not found'}, status=500) 
    
    
    @swagger_auto_schema(
        tags=["userank"],
        methods=['POST'],
        operation_summary="userank POST with Params",
        request_body = openapi.Schema(
        title= "Create Dataset",
        type=openapi.TYPE_OBJECT, 
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='string', example="test"),
            'deposit': openapi.Schema(type=openapi.TYPE_INTEGER, description='int', example=1111),
            'earning_rate': openapi.Schema(type=openapi.TYPE_INTEGER, description='int', example=11)
            # 'earning_rate': openapi.Schema(type=openapi.TYPE_STRING, description='start_date', example="2022-05-27T12:48:07.256Z", format="YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]"),
            # 'start_date': openapi.Schema(type=openapi.TYPE_STRING, description='start_date', example="2022-05-27 12:48:07", format="YYYY-MM-DD HH:MM:ss"),
        }),
        responses={200: 'Item was created'})
    @api_view(['POST'])
    def post_params_api(request):
        request_json = request.data
        logger.info("post_params_api : {}".format(json.dumps(request_json, indent=2)))
        
        try:
            # --
            userRankCreate = userRank.objects.create(
                username = request_json.get("username"),
                deposit =  request_json.get("deposit"),
                earning_rate = request_json.get("earning_rate"),
            )
            return JsonResponse({"results": 'Item was created'}, status=200)
        except Exception as e:
            logger.error(e)
            return JsonResponse({"results": str(e)}, status=500)