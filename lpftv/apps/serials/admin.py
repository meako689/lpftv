from django.contrib import admin
from apps.serials.models import Serial, Episode, News, RImage 

class SerialAdmin(admin.ModelAdmin):
    list_filter = ['name']
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'pub_date')

class EpisodeAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ('name', 'pub_date')

class NewsAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ('name','pub_date')

class RImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'to_url')

admin.site.register(Serial, SerialAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(RImage, RImageAdmin)

