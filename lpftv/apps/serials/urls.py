from django.conf.urls.defaults import *

urlpatterns = patterns('apps.serials.views',
    (r'^$', 'index'),
    (r'^serial/$','show_serial'),
    (r'^serial/(?P<s_id>\d+)/$', 'serial_dateil'),
)

