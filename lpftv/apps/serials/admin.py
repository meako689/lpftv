from django.contrib import admin
from apps.serials.models import Serial, Movie, NewsRecord 

class SerialAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ('name', 'pub_date')

class MovieAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ('name', 'pub_date')

class NewsAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ('name','pub_date')

admin.site.register(Serial, SerialAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(NewsRecord, NewsAdmin)

