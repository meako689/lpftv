from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'views.index'),
    (r'^home/', include('apps.serials.urls')),
    (r'^admin/', include(admin.site.urls)),
)
