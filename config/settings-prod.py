
'''
https://stackoverflow.com/questions/49235486/how-to-properly-runserver-on-different-settings-for-django
'''
from .settings import *

# --
# Prod settigs
# --

# --
# Custom Settings
# --

GLOBAL_ES_HOST = 'http://localhost:9209'
GLOBAL_HOST_URL = 'http://localhost:9999'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',  # database name
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': os.getenv("REDIS_HOST", "localhost-prod"),
        'PORT': '15432',
    }
}


GLOBAL_REDIS_URL = "redis://{}:{}/{}".format(os.getenv("REDIS_HOST", "localhost-prod"), os.getenv("REDIS_PORT", 6379),os.getenv("REDIS_DATABASE", 0)),
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