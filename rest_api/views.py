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
from .injector import SearchOmniHandlerInject, logger


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
            'x': openapi.Schema(type=openapi.TYPE_STRING, description='string', example="test_x"),
            'y': openapi.Schema(type=openapi.TYPE_STRING, description='string', example="test_y"),
            # 'start_date': openapi.Schema(type=openapi.TYPE_STRING, description='start_date', example="2022-05-27T12:48:07.256Z", format="YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]"),
            'start_date': openapi.Schema(type=openapi.TYPE_STRING, description='start_date', example="2022-05-27 12:48:07", format="YYYY-MM-DD HH:MM:ss"),
        }),
        # responses={200: Schema(type=TYPE_OBJECT)})
        responses={200: 'Item was created'}
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
            SearchOmniHandlerInject.search()
            return JsonResponse({'message' : request_json})
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
    def delete_params_api(request, pk):
        """using this api for delete with {id}"""
        if pk is None:
            # logger.info("userRanks : {}".format(userRanks))
            return JsonResponse({"results": userRanksList}, status=200)
        logger.info('request : {}'.format(request))
        logger.info('PK : {}'.format(pk))
        # student = get_object_or_404(Student, pk=pk)
        return Response({"date_joined": 'test'}, 200)