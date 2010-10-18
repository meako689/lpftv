from django.conf import settings
from django.db import models
from markdown import markdown
import Image, os

class Serial(models.Model):
    name = models.CharField(max_length = 50, verbose_name = "Serials' name")
    short_describe = models.TextField(verbose_name = "Short describe")
    full_describe = models.TextField(verbose_name = "Full describe")
    origin_img = models.ImageField(upload_to = "photos", blank = True) 
    last_img = models.ImageField(upload_to = "photos", editable = False, default = "")
    pub_date = models.DateTimeField()

    def get_small_image(self):
        return self.origin_img.path[:-4]+"_small.jpeg"

    def get_small_name(self):
        return self.origin_img.name[:-4]+"_small.jpeg"

    def mark_short_describe(self):
        return markdown(self.short_describe)

    def pre_save(self):
        try:
            if os.path.exists(self.last_img.path):
                os.remove(self.last_img.path)
            if os.path.exists(get_small_image(self)):
                os.remove(get_small_image(self))
        except:
            None
        self.last_img = self.origin_img

    def save(self):
        size = 128
        models.Model.save(self)
        try:
            im = Image.open(self.origin_img.path)
            im.thumbnail((size, size), Image.ANTIALIAS)
            im.save(self.origin_img.path[:-4] + "_small.jpeg", "jpeg")
        except IOError:
            print "IOError: cann't resize image "

    def delete(self, save=True):
        name = self.origin_img.path[:4] + "_small.jpeg"
        if os.path.exists(name):
            os.remove(name)
        model.Model.delete(self, save)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('-pub_date',)

class Movie(models.Model):
    serial = models.ForeignKey(Serial)
    name = models.CharField(max_length = 50, verbose_name = "Serial's name")
    short_describe = models.TextField(verbose_name = "Short describe")
    origin_img = models.ImageField(upload_to = "photos")
    movie = models.FileField(upload_to = "serials")
    pub_date = models.DateTimeField()
    last_img = models.ImageField(upload_to = "photos", editable = False, default = "")
    
    def pre_save(self):
        try:
            if os.path.exists(self.last_img.path):
                os.remove(self.last_img.path)
            if os.path.exists(self.last_img.path[:-4]+"_small.jpeg"):
                os.remove(self.last_img.path[:-4]+"_small.jpeg")
        except:
            None
        self.last_img = self.origin_img

    def save(self):
        size = 128
        models.Model.save(self)
        try:
            im = Image.open(self.origin_img.path)
            im.thumbnail((size, size), Image.ANTIALIAS)
            im.save(self.origin_img.path[:-4] + "_small.jpeg", "jpeg")
        except IOError:
            print "IOError: cann't resize image "

    def delete(self, save=True):
        name = self.origin_img.path[:4] + "_small.jpeg"
        if os.path.exists(name):
            os.remove(name)
        model.Model.delete(self, save)


    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.name

class New(models.Model):
    name = models.CharField(max_length=100, verbose_name = "New's name")
    describe = models.TextField(verbose_name = "Short describe")
    text = models.TextField(verbose_name = "News")
    pub_date = models.DateTimeField("Publicated date")

    class Meta:
         ordering = ('-pub_date',)

    def __unicode__(self):
        return name

class SComment(models.Model):
    author = models.CharField(max_length = 50, verbose_name = "Author")
    text = models.TextField(verbose_name = "Comment")
    link = models.ForeignKey(Serial)
    pub_date = models.DateTimeField("Comment's date")

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return author + ": " +links

class MComment(models.Model):
    author = models.CharField(max_length = 50, verbose_name = "Author")
    text = models.TextField(verbose_name = "Comment")
    link = models.ForeignKey(Movie)
    pub_date = models.DateTimeField("Comment's date")

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return author + ": " +links

class NComment(models.Model):
    author = models.CharField(max_length = 50, verbose_name = "Author")
    text = models.TextField(verbose_name = "Comment")
    link = models.ForeignKey(New)
    pub_date = models.DateTimeField("Comment's date")

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return author + ": " +links

def pre_save(sender, **kwargs):
    sobject = kwargs['instance']
    try:
        sobject.pre_save()
    except:
        None

models.signals.pre_save.connect(pre_save)

