__author__ = 'emam'
from base import *

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'youchoose',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '54.171.247.231',  # '127.0.0.1'
        'PORT': '5432',  # '5556'
    }
}
