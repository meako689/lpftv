# Django settings for lpftv project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = os.path.join(PROJECT_PATH,'base.db')             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

TIME_ZONE = 'Europe/Kiev'
LANGUAGE_CODE = 'uk-ua'
SITE_ID = 1
USE_I18N = True
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'static')
MEDIA_URL = '/media_url/'
ADMIN_MEDIA_PREFIX = '/multi/'

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

    'apps.serials',
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
