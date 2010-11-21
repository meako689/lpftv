from markdown import markdown
from django.views.generic.list_detail import object_detail
from django.shortcuts import render_to_response, get_object_or_404
from apps.serials.models import Serial, Episode, News
from django.conf import settings
from django.template import RequestContext

def index(request):
     serials = Serial.objects.all()[:5]
     news = News.objects.all() 
     return render_to_response("serials/index.html", {'news': news, 'serials': serials}, context_instance=RequestContext(request))

def show_news(request):
     news = News.objects.all()
     return render_to_response("serials/news.html", {'news': news}, context_instance=RequestContext(request))

def show_serial(request):
     serials = Serial.objects.all()
     return render_to_response("serials/serials.html", {'serials': serials, 'default_width': settings.IMAGE_XY}, context_instance=RequestContext(request))

def serial_detail(request, s_id):
     serials = get_object_or_404(Serial, id = s_id)
     episodes = Episode.objects.filter(serial = serials)
     return render_to_response("serials/serial_detail.html", {'serial': serials, 'episodes': episodes, 'next': serials.get_absolute_url()}, context_instance=RequestContext(request))

def episode_detail(request ,s_id, e_id):
    return object_detail(request,
        queryset = Episode.objects.all(),
        object_id = e_id,
        template_name = "serials/episode_detail.html"
        )

def news_detail(request, n_id):
     news = get_object_or_404(News, id = n_id)
     return render_to_response("serials/news_detail.html", {'news': news, 'next': news.get_absolute_url()}, context_instance=RequestContext(request))

def find(request):
    find_str = request.GET['find']
    return render_to_response("serials/find.html", {'find_str': find_str}, context_instance=RequestContext(request))
