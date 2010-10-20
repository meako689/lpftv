from markdown import markdown
from django.shortcuts import render_to_response
from apps.serials.models import Serial, NewsRecord

def index(request):
     serials = Serial.objects.all()[:5]
     for serial in serials:
         serial.mark_short = markdown(serial.short_describe) 
         serial.small_img = serial.get_small_url()
     news = NewsRecord.objects.all() 
     return render_to_response("index.html", {'news': news, 'serials': serials})

def show_news(request):
     news = NewsRecord.objects.all()
     return render_to_response("news.html", {'news': news})

def show_serial(request):
     serials = Serial.objects.all()
     for serial in serials:
         serial.mark_short = markdown(serial.short_describe) 
         serial.small_img = serial.get_small_url() 
     return render_to_response("serials.html", {'serials': serials})

def serial_dateil(request, s_id):
     return render_to_response("base.html")

def news_dateil(request, n_id):
     return render_to_response("base.html")
