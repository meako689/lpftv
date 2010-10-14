from django.db import models

class Serial(models.Model):
    name = models.CharField(max_length = 50, verbose_name = "Serials' name")
    short_describe = models.TextField(verbose_name = "Short describe")
    full_describe = models.TextField(verbose_name = "Full describe")
    origin_img = models.ImageField(upload_to = "photos") 
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return self.name

class Movie(models.Model):
    serial = models.ForeignKey(Serial)
    name = models.CharField(max_length = 50, verbose_name = "Serial's name")
    short_describe = models.TextField(verbose_name = "Shor describe")
    full_describe = models.TextField(verbose_name = "Full describe")
    origin_img = models.ImageField(upload_to = "photos")
    movie = models.FileField(upload_to = "serials")
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return self.name

