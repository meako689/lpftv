from django.contrib import admin
from apps.serials.models import Serial, Movie, New, SComment

class SerialAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ('name', 'pub_date')

class MovieAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ('name', 'serial', 'pub_date')

class NewAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ('name', 'pub_date')

class SCommentAdmin(admin.ModelAdmin):
    list_filter = ['author' , 'link', 'pub_date']
    list_display = ('author', 'link', 'pub_date')

admin.site.register(Serial, SerialAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(New, NewAdmin)
admin.site.register(SComment, SCommentAdmin)

