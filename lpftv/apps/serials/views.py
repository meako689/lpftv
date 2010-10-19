from markdown import markdown
from django.shortcuts import render_to_response
from apps.serials.models import Serial

def index(request):
     return render_to_response("base.html")

def show_news(request):
     return render_to_response("base.html")

def show_serial(request):
     serials = Serial.objects.all()
     for serial in serials:
         serial.mark_short = markdown(serial.short_describe) 
         serial.small_img = serial.get_small_url() 
     return render_to_response("serials.html", {'serials': serials})

def serial_dateil(request, s_id):
     return render_to_response("base.html")

