from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

# --
# import rest_api models, injector to ui app
from rest_api.models import Student
from rest_api.injector import logger
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage

# --
# Search
from django.views.decorators.csrf import csrf_exempt
from rest_api.views import SearchView
from rest_api.injector import URL_HOST
from .controller.Rule import Rule
import json
import requests

RequestObject = Rule()

def rest_apis(request, page=20):
  '''
  # Default index.html
  template = loader.get_template('default/index.html')
  return HttpResponse(template.render())
  '''
  students = Student.objects.all().order_by('id')
  paginator = Paginator(students, page)
  try:
    students = paginator.page(page)
  except (EmptyPage, InvalidPage):
    students = paginator.page(paginator.num_pages)
  
  '''
  paginator = Paginator(movie_list , 100) # Show 100 movies per page.

  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  return render(request, 'movies.html', {'page_obj': page_obj})
  '''
  
#   logger.info("students : {}".format(json.dumps(students, indent=2)))
  # template = loader.get_template('default/all_students.html')
  
  context = {
    'students': students,
    'copystudents' : students
  }
  '''
  context = {
    'students': [{'name': 'test', 'grade': 'test'}],
    'copystudents' : students
  }
  '''
#   return HttpResponse(template.render(context, request))
  # return render(request, 'default/all_students.html', context)
  return render(request, 'default/dttables.html', context)
  # return render(request, 'search/index.html', context)



@csrf_exempt
def rest_search_main(request):
  return render(request, 'search/index.html', None)

@csrf_exempt
def rest_search_apis(request):

  logger.info(request)

  result = requests.post(url="{}/rest_api/es/search".format(URL_HOST), 
                         data=json.dumps(RequestObject.get_payload()), 
                         headers=RequestObject.get_header()
                         )
  # logger.info(result.content, type(result.content)) # (<class 'bytes'>,)
  logger.info(json.dumps(result.json(), indent=2))
  # logger.info(json.dumps(RequestObject.get_search_result()['hits'], indent=2))
  
  hits = []
  # response_results_json = result.json()
  response_results_json = RequestObject.get_search_result()
  for hit in response_results_json['hits']:
    each_dict = hit
    # print(hit)
    if '_source' in each_dict: 
      each_dict.update({"source" : hit['_source']})
      del each_dict['_source']
    hits.append(each_dict)
    
  context = {
    'response': hits,
    'total' : int(response_results_json['total']['value']),
    # 'keyword': keyword
  }
  return render(request, 'search/index.html', context)
