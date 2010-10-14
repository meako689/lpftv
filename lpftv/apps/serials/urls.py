from django.conf.urls.defaults import *

urlpatterns = patterns('apps.serials.views',
    (r'^serial/$','show_serial'),
)

