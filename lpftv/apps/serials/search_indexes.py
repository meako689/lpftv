import datetime
from haystack.indexes import *
from haystack import site
from apps.serials.models import Serial


class SerialIndex(SearchIndex):
    name = CharField(document=True, use_template=True)
    pub_date = DateTimeField(model_attr='pub_date')

    def get_queryset(self):
        return Serial.objects.all()


site.register(Serial, SerialIndex)
