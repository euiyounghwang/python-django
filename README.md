### Python-Search Project with Django



Install Poerty
```
https://python-poetry.org/docs/?ref=dylancastillo.co#installing-with-the-official-installer
```

Using Poetry: Create the virtual environment in the same directory as the project and install the dependencies:
```
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
```


Create project
```
source .venv/bin/activate
poetry run python manage.py migrate 
# Create rest_api app
python manage.py startapp rest_api
```