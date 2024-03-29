
'''
https://stackoverflow.com/questions/49235486/how-to-properly-runserver-on-different-settings-for-django
'''
from .settings import *

# --
# Dev settigs
# --

# --
# Custom Settings
# --

GLOBAL_ES_HOST = os.getenv('ES_HOST', "http://localhost:9203")
GLOBAL_HOST_URL = 'http://localhost:9999'

# https://github.com/PylotStuff/django-mongodb-postgres
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',  # database name
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': os.getenv("REDIS_HOST", "localhost"),
        'PORT': '15432',
    },
    "mongo_db": {
        "ENGINE": "djongo",
        "NAME": "mongo-local",
        "CLIENT": {
            "host": os.getenv('MONGO_DB_HOST', "127.0.0.1"),
            "port": int(os.getenv('MONGO_DB_PORT', 27017)),
            "username": "postgres",
            "password": "1234",
        },
        'TEST': {
            'MIRROR': 'default',
        },
    }
}

GLOBAL_REDIS_URL = "redis://{}:{}/{}".format(os.getenv("REDIS_HOST", "localhost"), os.getenv("REDIS_PORT", 6379),os.getenv("REDIS_DATABASE", 0)),
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION':  GLOBAL_REDIS_URL, # Change this according to your Redis server's URL & port
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
        # "KEY_PREFIX": "imdb",
        "TIMEOUT": 60 * 15,  # in seconds: 60 * 15 (15 minutes)
    }
}