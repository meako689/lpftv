from django.http import HttpResponse
from django.shortcuts import render_to_response
from apps.serials.models import Serial

def show_serial(request):
     serials = Serial.objects.all()
     for serial in serials:
         serial.small_image = serial.get_small_image()
         serial.mark_short = serial.mark_short_describe()
     return render_to_response("serials.html", {'serials': serials})

