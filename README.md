### Python-Search Project with Django

__Why Django REST Framework?__
There are many frameworks for building REST APIs, but we’re gonna use the Django Rest Framework by the following reasons:
- The Web browsable API is a huge usability win for developers.
- Authentication policies including packages for OAuth1a and OAuth2.
- Serialization supports both ORM and non-ORM data sources.
- Customizable all the way down – just use regular function-based views if you don’t need the more powerful features.
- Extensive documentation, and great community support.
- Used and trusted by internationally recognised companies including Mozilla, Red Hat, Heroku, and Eventbrite.

![Alt text](./screenshots/Django-RESTAPI-Architecture.png)

Guide
```
https://www.django-rest-framework.org/
https://cntechsystems.tistory.com/66
https://velog.io/@zueon/DRF-%EA%B8%B0%EC%B4%88
```


Install Poerty
```
https://python-poetry.org/docs/?ref=dylancastillo.co#installing-with-the-official-installer
```

Using Poetry: Create the virtual environment in the same directory as the project and install the dependencies:
```
django-admin startproject python-django
poetry config virtualenvs.in-project true
poetry init
```


Create virtualenv
```
python -m venv .venv
source .venv/bin/activate
```


Poetry install
```
poetry install
poetry add djangorestframework
```


Create project
```
source .venv/bin/activate
poetry run python manage.py migrate 
# Create rest_api app
python manage.py startapp rest_api
# Create book rest_api app
python manage.py startapp book_rest_api
```

Run server
```
python manage.py runserver 9999
```

URL
```
# Django
http://localhost:9999/

# djangorestframework (DRF)
http://localhost:9999/rest_api/swagger/

# Prometheus
https://hodovi.cc/blog/django-monitoring-with-prometheus-and-grafana/
http://localhost:9999/rest_api/prometheus/metrics
```