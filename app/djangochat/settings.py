from pathlib import path
from telnetlib import logout
import os

# build paths inside the project like this: base_dir / 'subdir'.
base_dir = path(__file__).resolve().parent.parent


# quick-start development settings - unsuitable for production
# see https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# security warning: keep the secret key used in production secret!
secret_key = 'django-insecure-!79n+mp+d)1-=z7w5ee9f5*74mhqbene^c*89j@(1gsot5&t@o'

# security warning: don't run with debug turned on in production!
debug = true

allowed_hosts = []

logout_redirect_url = '/'
login_redirect_url = '/rooms/'
login_url = '/login/'


# application definition

installed_apps = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'core',
    'room',
]

middleware = [
    'django.middleware.security.securitymiddleware',
    'django.contrib.sessions.middleware.sessionmiddleware',
    'django.middleware.common.commonmiddleware',
    'django.middleware.csrf.csrfviewmiddleware',
    'django.contrib.auth.middleware.authenticationmiddleware',
    'django.contrib.messages.middleware.messagemiddleware',
    'django.middleware.clickjacking.xframeoptionsmiddleware',
]

root_urlconf = 'djangochat.urls'

templates = [
    {
        'backend': 'django.template.backends.django.djangotemplates',
        'dirs': [],
        'app_dirs': true,
        'options': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

wsgi_application = 'djangochat.wsgi.application'
asgi_application = 'djangochat.asgi.application'

channel_layers = {
    'default': {
        'backend': 'channels.layers.inmemorychannellayer'
    }
}


# database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

databases = {
    'default': {
        'engine': 'django.db.backends.postgresql',
        'name': os.environ.get('postgres_name'),
        'user': os.environ.get('postgres_user'),
        'password': os.environ.get('postgres_password'),
        'host': 'db',
        'port': 5432,
    }
}

# password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

auth_password_validators = [
    {
        'name': 'django.contrib.auth.password_validation.userattributesimilarityvalidator',
    },
    {
        'name': 'django.contrib.auth.password_validation.minimumlengthvalidator',
    },
    {
        'name': 'django.contrib.auth.password_validation.commonpasswordvalidator',
    },
    {
        'name': 'django.contrib.auth.password_validation.numericpasswordvalidator',
    },
]


# internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

language_code = 'en-us'

time_zone = 'utc'

use_i18n = true

use_tz = true


# static files (css, javascript, images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

static_url = 'static/'

# default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

default_auto_field = 'django.db.models.bigautofield'
