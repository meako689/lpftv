import datetime
from haystack.indexes import *
from haystack import site
from apps.serials.models import Serial, Episode, News


class EpisodeIndex(SearchIndex):
    name = CharField(document=True, use_template=True)
    full_description = CharField()
    pub_date = DateTimeField(model_attr='pub_date')

    def get_queryset(self):
        return Episode.objects.all()

class SerialIndex(EpisodeIndex):
    short_description = CharField()

    def get_queryset(self):
        return Serial.objects.all()

class NewsIndex(SearchIndex):
    name = CharField(document=True, use_template=True)
    short_description = CharField()
    full_description = CharField()
    pub_date = DateTimeField(model_attr="pub_date")

    def get_queryset(self):
        return News.objects.all()


site.register(Episode, EpisodeIndex)
site.register(Serial, SerialIndex)
site.register(News, NewsIndex)
