from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'views.index'),
    (r'^home/', include('apps.serials.urls')),
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^media_url/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DOC_ROOT })
)
