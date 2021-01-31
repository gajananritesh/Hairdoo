# Python imports
from os.path import abspath, basename, dirname, join, normpath
import sys
from django.urls import reverse



# ##### PATH CONFIGURATION ################################

# fetch Django's project directory
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# fetch the project_root
PROJECT_ROOT = dirname(DJANGO_ROOT)

# the name of the whole site
SITE_NAME = basename(DJANGO_ROOT)

# collect static files here
STATIC_ROOT = join(PROJECT_ROOT, 'run', 'static')

# collect media files here
MEDIA_ROOT = join(PROJECT_ROOT, 'run', 'media')

# look for static assets here
STATICFILES_DIRS = [
    join(PROJECT_ROOT, 'apps','customadmin','static'),
]

# look for templates here
# This is an internal setting, used in the TEMPLATES directive
PROJECT_TEMPLATES = [
    join(PROJECT_ROOT, 'templates'),
]

# add apps/ to the Python path
sys.path.append(normpath(join(PROJECT_ROOT, 'apps')))


# ##### APPLICATION CONFIGURATION #########################


LOCAL_APPS = [
    'authentication',
    'social_account',
    'order',
    'payment',
    'customadmin',
    
]


THIRD_PARTY = [
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'widget_tweaks',

]

# these are the apps
DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + THIRD_PARTY + LOCAL_APPS


# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# template stuff
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': PROJECT_TEMPLATES,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'customadmin.context_processor.get_user_count',
                'customadmin.context_processor.get_order_number',
                # 'allauth.account.auth_backends.AuthenticationBackend',
            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': (
        'rest_framework.pagination.LimitOffsetPagination'
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'SEARCH_PARAM': 'q',
}


# SITE ID
SITE_ID = 1

REST_USE_JWT = True

# Internationalization
USE_I18N = False


LOGIN_REDIRECT_URL = 'core:homepage'
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = "account_login"

# custom-admin
LOGIN_URL = "auth:auth_login"
LOGOUT_REDIRECT_URL = "auth:auth_login"
# ##### SECURITY CONFIGURATION ############################

# We store the secret key here
# The required SECRET_KEY is fetched at the end of this file
SECRET_FILE = normpath(join(PROJECT_ROOT, 'run', 'SECRET.key'))

# these persons receive error notification
ADMINS = (
    ('your name', 'your_name@example.com'),
)
MANAGERS = ADMINS


# ##### DJANGO RUNNING CONFIGURATION ######################

# the default WSGI application
WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME

# the root URL configuration
ROOT_URLCONF = '%s.urls' % SITE_NAME

# the URL for static files
STATIC_URL = 'customadmin/static/'
#STATIC_ROOT = '/run/static/'
# the URL for media files
MEDIA_URL = '/media/'
#MEDIA_ROOT = '/run/media/'
# AUTH_USER_MODEL = 'authentication.Account'

# ##### DEBUG CONFIGURATION ###############################
DEBUG = False

AUTH_USER_MODEL = 'authentication.Account'


# STRIPE SCRET KEY
STRIPE_KEY = 'sk_test_M59oeSkIQEUMGT9MEXaFgTzX00Wy4c7Ptb'
PUBLIC_KEY = 'pk_test_OpVX8vOkAfUNbP0G9pcE6oFW00KMPHzg6z'

# finally grab the SECRET KEY

try:
    SECRET_KEY = open(SECRET_FILE).read().strip()
except IOError:
    try:
        from django.utils.crypto import get_random_string
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!$%&()=+-_'
        SECRET_KEY = get_random_string(50, chars)
        with open(SECRET_FILE, 'w') as f:
            f.write(SECRET_KEY)
    except IOError:
        raise Exception('Could not open %s for writing!' % SECRET_FILE)


# TWILIO CREDS
ACCOUNT_SID = 'AC336188965497efb45cb618d198c90412'
AUTH_TOKEN = '0aa0b126ff92bb5abf669cfd2a606029'
NUMBER = "+14434007472"
