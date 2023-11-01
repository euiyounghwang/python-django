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
from .controller.Rule import Rule
from .service.SearchHandler import UI_SearchHandler
import json
import requests

RequestObject = Rule()
search_handler = UI_SearchHandler(logger, RequestObject)

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
  return render(request, 'search/search.html', None)

@csrf_exempt
def rest_search_apis(request):
  '''
  Template
  '''
  keyword = ''
  logger.info(request)
  if request.POST.get("keyword"):
    logger.info(request.POST.get("keyword"))
    keyword = request.POST.get("keyword")
    # RequestObject.get_payload()['query_string'] = keyword
  else:
    logger.warn("It's not processing from SEARCH.HTML")
    
  pit = request.POST.get("pit")
   
  context = search_handler.Search(keyword, pit)
  # logger.info('context : {}'.format(context))
  return render(request, 'search/index.html', context)
