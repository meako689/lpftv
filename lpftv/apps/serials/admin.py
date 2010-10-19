from django.contrib import admin
from apps.serials.models import Serial 

class SerialAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ('name', 'pub_date')

admin.site.register(Serial, SerialAdmin)

