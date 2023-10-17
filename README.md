### Python-Search Project with Django

Guide
```
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
http://localhost:9999/book_rest_api/swagger/
```