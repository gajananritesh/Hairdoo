# Python imports
from os.path import join

# project imports
from .common import *

# uncomment the following line to include i18n
# from .i18n import *


# ##### DEBUG CONFIGURATION ###############################
DEBUG = True

# allow all hosts during development
ALLOWED_HOSTS = ['*']


# ##### DATABASE CONFIGURATION ############################
# postgres://postgres:qqtgArrPj4FNVeQ08hqH@python-citrusbug-2020.cnnafiiwnwzs.ap-south-1.rds.amazonaws.com:5432/hairdoo
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hairdoo',
        'USER': 'postgres',
        'HOST': 'python-citrusbug-2020.cnnafiiwnwzs.ap-south-1.rds.amazonaws.com',
        'PASSWORD': 'qqtgArrPj4FNVeQ08hqH',
        'PORT': '5432'
    }
}

# ##### APPLICATION CONFIGURATION #########################

SITE_URL = 'http://3.6.9.168:9300'

INSTALLED_APPS = DEFAULT_APPS


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'webmaster.citrusbug@gmail.com'
EMAIL_HOST_BCC = 'rahul.citrusbug@gmail.com'
EMAIL_HOST_PASSWORD = 'mdgutpvqfeglinbh'
EMAIL_USE_TLS = True
