# Django settings for lpftv project.
import sys
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
FILE_UPLOAD_PERMISSIONS = 0666

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_PATH)
sys.path.insert(0, os.path.join(PROJECT_PATH, 'apps'))

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

#DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#DATABASE_NAME = os.path.join(PROJECT_PATH,'base.db')             # Or path to database file if using sqlite3.

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3',
        'NAME': os.path.join(PROJECT_PATH, 'base.db'),
        'HOST': '',
        'USER': '',
    }
}

TIME_ZONE = 'Europe/Kiev'
LANGUAGE_CODE = 'uk-ua'
SITE_ID = 1
USE_I18N = True
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'static')
MEDIA_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'yr1@ixe6-um0zoowcu#h=#mfbooc@wm47so5j$uwb975cg5kz1'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.csrf.middleware.CsrfMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

STATIC_DOC_ROOT = os.path.join(PROJECT_PATH, 'static')

ROOT_URLCONF = 'lpftv.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates',),
    os.path.join(PROJECT_PATH, 'media/tempaltes'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth", 
    "django.core.context_processors.debug", 
    "django.core.context_processors.i18n", 
    "django.core.context_processors.media", 
    "django.core.context_processors.request", 
    'django.core.context_processors.media',
    'apps.serials.context_processors.find_text'
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.comments',
    'django.contrib.markup',
    'django.contrib.flatpages',
    
    'south',
    'haystack',

    'lpftv.apps.serials',
)

#Haystack configuration
HAYSTACK_SITECONF = 'apps.search_sites'
HAYSTACK_SEARCH_ENGINE = 'whoosh'
#It's must be real path to dir where indexes was saved`
HAYSTACK_WHOOSH_PATH = MEDIA_ROOT+'/index'

#It's size for thumb image
IMAGE_XY = 100
SERIAL_IMAGE_XY = 150
#Default image
IMAGE_DEFAULT = MEDIA_URL + "photos/default.jpg"
try:
    from settings_local import *
except ImportError, e:
    #sys.stderr.write('settings_local.py not found. Using default settings\n')
    #sys.stderr.write('%s: %s\n\n' % (e.__class__.__name__, e))
    pass

