from django.conf.urls.defaults import *

urlpatterns = patterns('apps.serials.views',
    (r'^$', 'index'),
    (r'^serial/$','show_serial'),
    (r'^news/$', 'show_news'),
    url(r'^serial/(?P<s_id>\d+)/$', 'serial_dateil', name="serial_dateil"),
    url(r'^news/(?P<n_id>\d+)/$', 'news_dateil', name="news_dateil"),
)

