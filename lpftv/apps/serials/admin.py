from django.contrib import admin
from apps.serials.models import Serial, Episode, News, RImage 

def series_count(obj):
    return ("%s" % obj.episode_set.count())
series_count.short_description = 'Series'
class SerialAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'pub_date',series_count)
    fields = ('name', 
        'short_description', 
        'full_description',
        'origin_img',
        'pub_date',
        'slug')

class EpisodeAdmin(admin.ModelAdmin):
    list_filter = ['serial']
    list_display = ('__unicode__', 'pub_date')

class NewsAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ('name','pub_date')

class RImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'to_url')

admin.site.register(Serial, SerialAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(RImage, RImageAdmin)

