from markdown import markdown
from django.shortcuts import render_to_response, get_object_or_404
from apps.serials.models import Serial, Movie, NewsRecord
from django.conf import settings
from django.template import RequestContext

def index(request):
     serials = Serial.objects.all()[:5]
     news = NewsRecord.objects.all() 
     return render_to_response("index.html", {'news': news, 'serials': serials}, context_instance=RequestContext(request))

def show_news(request):
     news = NewsRecord.objects.all()
     return render_to_response("news.html", {'news': news}, context_instance=RequestContext(request))

def show_serial(request):
     serials = Serial.objects.all()
     return render_to_response("serials.html", {'serials': serials}, context_instance=RequestContext(request))

def serial_detail(request, s_id):
     serials = get_object_or_404(Serial, id = s_id)
     movies = Movie.objects.filter(serial = serials)
     return render_to_response("serial_detail.html", {'serial': serials, 'movies': movies, 'next': serials.get_absolute_url()}, context_instance=RequestContext(request))

def news_detail(request, n_id):
     news = get_object_or_404(NewsRecord, id = n_id)
     return render_to_response("news_detail.html", {'news': news, 'next': news.get_absolute_url()}, context_instance=RequestContext(request))
