from django.conf.urls.defaults import *

urlpatterns = patterns('apps.serials.views',
    url(r'^$', 'index', name = 'index'),
    url(r'^find/$', 'find', name='find'),
    url(r'^series/$','show_serial', name = 'serials_index'),
    url(r'^news/$', 'show_news', name = 'news_index'),
    url(r'^series/(?P<s_id>\d+)/$', 'serial_detail', name="serial_detail"),
    url(r'^series/(?P<s_id>\d+)/(?P<e_id>\d+)/$', 'episode_detail', name="episode_detail"),
    url(r'^news/(?P<n_id>\d+)/$', 'news_detail', name="news_detail"),
)

