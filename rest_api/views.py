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

from .models import Student
from .serializers import StudentSerializer

logger = create_log()


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


@api_view(["GET",])
def get_student_date_joined(request, pk):
    """A simple view to return the date and time a student signed up"""

    student = get_object_or_404(Student, pk=pk)
    return Response({"date_joined": student.date}, 200)



@api_view(["GET",])
def get_note(request):
    try:
        # obj_id = request.GET.get('obj_id')
        # logger.info('request : {}'.format(obj_id))
        return Response({'message' : 'Get: hello, world!'})
    except Exception as e:
        logger.error(e)

@api_view(["GET",])
def get_note_joined(request, pk):
    try:
        logger.info('request : {}'.format(pk))
        return Response({'message' : 'Get: hello, world! [From : {}]'.format(pk)})
    except Exception as e:
        logger.error(e)


@swagger_auto_schema(
    tags=["Search"],
    methods=['POST'],
    operation_summary="Sum of Two numbers",
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
    responses={200: 'Item was created'})
    # responses={
    #     200: openapi.Schema(
    #         type=openapi.TYPE_INTEGER,
    #         title="s"
    #     )
#     # })
@api_view(['POST'])
def get_note_post_joined(request):
    try:
        # print(request.data)
        request_json = request.data
        # tutorial_data = JSONParser().parse(request)
        print('request : {}'.format(json.dumps(request_json, indent=2)))
        logger.info('request : {}'.format(json.dumps(request_json, indent=2)))
        return JsonResponse({'message' : 'Post: hello, world!'})
    except Exception as e:
        logger.error(e)




# Create your views here.
class TestView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['my custom tag'])
    def get(self, request):
        return Response("Swagger Interface Test")


class RestapiView(APIView):
    # serializer_class = ProductGetSerializer
    
    permission_classes = [permissions.AllowAny]
    
    # @swagger_auto_schema(tags=['rest_api'], responses={200: Schema(type=TYPE_OBJECT)})
    # def get(self, request):
    #     try:
    #         logger.info('request helloAPI')
    #         return Response({'message' : 'Get: hello, world!'})
    #     except Exception as e:
    #         logger.error(e)
            
    
    obj_id_param = openapi.Parameter('obj_id', openapi.IN_QUERY, description="field id", type=openapi.TYPE_STRING)
    @swagger_auto_schema(tags=['rest_api'], metheod=['GET'], manual_parameters=[obj_id_param], responses={200: Schema(type=TYPE_OBJECT)})
    def get(self, request, obj_id=None):
        try:
            obj_id = request.GET.get('obj_id')
            logger.info('request : {}'.format(obj_id))
            return Response({'message' : 'Get: hello, world!'})
        except Exception as e:
            logger.error(e)
            
            
    # obj_id_param = openapi.Parameter('obj_id', openapi.IN_QUERY, description="field id", type=openapi.TYPE_STRING)
    # @swagger_auto_schema(tags=['rest_api'], metheod=['GET'], responses={200: Schema(type=TYPE_OBJECT)})
    # def get(self, request, obj_id):
    #     try:
    #         obj_id = request.GET.get('obj_id')
    #         logger.info('request : {}'.format(obj_id))
    #         return Response({'message' : 'Get: hello, world!'})
    #     except Exception as e:
    #         logger.error(e)
            
    
    @swagger_auto_schema(tags=['rest_api'], metheod=['POST'], request_body=openapi.Schema(
    title= "Create Dataset",
    type=openapi.TYPE_OBJECT, 
    properties={
        'x': openapi.Schema(type=openapi.TYPE_STRING, description='string', example="test_x"),
        'y': openapi.Schema(type=openapi.TYPE_STRING, description='string', example="test_y"),
        # 'start_date': openapi.Schema(type=openapi.TYPE_STRING, description='start_date', example="2022-05-27T12:48:07.256Z", format="YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]"),
        'start_date': openapi.Schema(type=openapi.TYPE_STRING, description='start_date', example="2022-05-27 12:48:07", format="YYYY-MM-DD HH:MM:ss"),
    }),
    # responses={200: Schema(type=TYPE_OBJECT)})
    responses={200: 'Item was created'})
    def post(self, request):
        try:
            # print(request.data)
            request_json = request.data
            # tutorial_data = JSONParser().parse(request)
            print('request : {}'.format(json.dumps(request_json, indent=2)))
            logger.info('request : {}'.format(json.dumps(request_json, indent=2)))
            return JsonResponse({'message' : 'Post: hello, world!'})
        except Exception as e:
            logger.error(e)

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
