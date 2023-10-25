from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from rest_api.models import Student
from rest_api.injector import logger

def rest_apis(request):
  '''
  # Default index.html
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
  '''
  students = Student.objects.all().values()
  logger.info("students : {}".format(students))
  template = loader.get_template('all_students.html')
  context = {
    'students': students,
  }
  return HttpResponse(template.render(context, request))

