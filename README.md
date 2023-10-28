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
# --
# Swagger
https://episyche.com/blog/how-to-create-django-api-documentation-using-swagger
https://pjs21s.github.io/vuejs-restframe/
```


Install Poerty
```
https://python-poetry.org/docs/?ref=dylancastillo.co#installing-with-the-official-installer
```

Using Poetry: Create the virtual environment in the same directory as the project and install the dependencies:
```bash
django-admin startproject python-django
poetry config virtualenvs.in-project true
poetry init
```


Create virtualenv
```bash
python -m venv .venv
source .venv/bin/activate
```


Poetry install
```bash
poetry install
poetry add djangorestframework
# For Swqgger
poetry add django-rest-swagger
poetry add drf-yasg
```

Add 'rest_framework' to your INSTALLED_APPS setting.
```bash
INSTALLED_APPS = [
    ...
    # --
    # Django Prometheus
    "django_prometheus",
    # --
    'rest_framework',
    # --
    # Add Swagger
    'rest_framework_swagger',
    'drf_yasg',
    # --
    "rest_api",
    'book_rest_api'		 
]
```

Create project
```bash
source .venv/bin/activate
poetry run python manage.py migrate 
# Create rest_api app
python manage.py startapp rest_api
# Create book rest_api app
python manage.py startapp book_rest_api
```

Run server
```bash
python manage.py runserver 9999
```

Django Admin Page (http://localhost:9999/admin)
```bash
python manage.py migrate

(.venv) ➜  python-django git:(master) ✗ python manage.py createsuperuser
System check identified some issues:

WARNINGS:
?: (urls.W005) URL namespace 'admin' isn't unique. You may not be able to reverse all URLs in this namespace
Username (leave blank to use 'euiyoung.hwang'): admin
Email address: marieuig@gmail.com
Password: 
Password (again): 
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

Add Model
```bash
# models.py
# -- Record & detect about the changing for the model
python manage.py makemigrations
# -- Update to DB if any changes in the model (this step requires in the Django)
python manage.py migrate

(.venv) ➜  python-django git:(master) ✗ python manage.py makemigrations
Migrations for 'rest_api':
  rest_api/migrations/0001_initial.py
    - Create model Student
    - Create model userRank
```


URL
```http
# Django
http://localhost:9999/

# Django UI
http://localhost:9999/rest_ui/

# djangorestframework (DRF) <- Instead of djangorestframework, build Swagger from config.urls (This above url's not working )
http://localhost:9999/rest_api/swagger/

# djangorestframework (DRF) &&  rest_framework_swagger, drf_yasg
http://localhost:9999/swagger/
http://localhost:9999/redoc/

# Prometheus
https://hodovi.cc/blog/django-monitoring-with-prometheus-and-grafana/
http://localhost:9999/rest_api/prometheus/metrics
```

Django search (Frontend)
- http://localhost:9999/rest_ui/
- view in rest_ui app is calling to rest_api (POST: /es/search) for searching from elasticsearch in rest_api app in Django project
- It does show you to retrieve texts

![Alt text](./screenshots/Django-rest_ui-search.png)

Postgres
```bash
# To be able to use PostgreSQL in Django we have to install a package called psycopg2.
poetry add psycopg2-binary

# Add this setting in settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'project',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

Gunicorn Serive Rigistry
```bash
sudo vi /etc/systemd/system/django-gunicorn.service

[Unit]
Description=gunicorn daemon
After=network.target

#--
[Service]
User=foo
Group=www-data
WorkingDirectory=/home/foo/django_test/repo
ExecStart=/Users/euiyoung.hwang/ES/Python_Workspace/python-django/.venv/bin/gunicorn \
        --workers 3 \
        --bind 0.0.0.0:9999 \
        config.wsgi:application

[Install]
WantedBy=multi-user.target
#--

# Run service
systemctl daemon-reload
# Autostart when rebooting
sudo systemctl enable django-gunicorn.service
systemctl start django-gunicorn

systemctl status django-gunicorn.service
● django-gunicorn.service - 
```