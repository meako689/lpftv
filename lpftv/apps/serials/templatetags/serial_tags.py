from django.conf import settings
from django import template
from apps.serials.models import Episode,Serial, RImage

register = template.Library()

@register.inclusion_tag("serials/tag_last_episodes.html")
def show_last_episodes():
    """Include last episodes"""
    episodes = Episode.objects.order_by('-pub_date')[:10]
    return {'episodes': episodes, 'MEDIA_URL':settings.MEDIA_URL}

@register.inclusion_tag("serials/tag_serials_list.html")
def serials_list():
    """show list of serials"""
    serials = Serial.objects.all()
    return {'serials':serials}

@register.inclusion_tag("serials/tag_rimages.html")
def rimage_init():
    """slideshow"""
    rimages = RImage.objects.all()
    return {'rimages': rimages}


