from django.contrib import admin
from apps.serials.models import Serial, Episode, News 

class SerialAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ('name', 'pub_date')

class EpisodeAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ('name', 'pub_date')

class NewsAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ('name','pub_date')

admin.site.register(Serial, SerialAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(News, NewsAdmin)

