# -*- coding: utf-8 -*-
from datetime import datetime
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
import Image, os

__docformat__ = "restructuredtext"

class CFilm(models.Model):
    """
    Base model for 'Episode' and 'Serial' models 
    """
    name = models.CharField(max_length = 50, verbose_name = "name")
    full_description = models.TextField(verbose_name = "Full description", blank = True)
    origin_img = models.ImageField(upload_to = "photos") 
    last_img = models.ImageField(upload_to = "photos", editable = False, default = "")
    pub_date = models.DateTimeField(default = datetime.now)

    def get_thumb_url(self):
        """Return url to small image"""
        return self.origin_img.url[:self.origin_img.url.rindex('.')]+ \
                ".small"+self.origin_img.url[self.origin_img.url.rindex('.'):]

    def get_thumb_path(self):
        """Return path in local disk to small image"""
        return self.origin_img.path[:self.origin_img.path.rindex('.')]+ \
            ".small"+self.origin_img.path[self.origin_img.path.rindex('.'):]

    def get_last_img_path(self):
        """This function used only in pre_save()"""
        try:
            return self.last_img.path[:self.last_img.path.rindex('.')]+ \
                ".small"+self.last_img.path[self.last_img.path.rindex('.'):]
        except: '' 

    def save(self):
        """Saving small image 'size'x'size' in local disk"""
        models.Model.save(self)
        size = 200
        try:
            im = Image.open(self.origin_img.path)
            im.thumbnail((size, size), Image.ANTIALIAS)
            im.save(self.get_thumb_path(), "jpeg") 
        except IOError:
            print "Error"



    def delete(self):
        """Remove images and remove record in database"""
        try:
            if os.path.exist(self.origin_img.path):
                os.remove(self.origin_img.path)
            if os.path.exists(self.get_thumb_path()):
                os.remove(self.get_thumb_path())
        except: pass

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('-pub_date',)


def remove_imgs(sender, instance, *args, **kwargs):
    """Remove old images"""
    if instance:
        try: 
            if os.path.exists(instance.get_last_img_path()):
                os.remove(instance.get_last_img_path())
            if os.path.exists(instance.last_img.path):
                os.remove(instance.last_img.path)
        except: pass 
        instance.last_img = instance.origin_img


class Serial(CFilm):
    """Contains serial description and movie"""
    short_description = models.TextField(verbose_name = "Short description")

    def get_absolute_url(self):
        return reverse('serial_detail', args=[self.id])

class Episode(CFilm):
    """This model is for episode"""
    serial = models.ForeignKey(Serial)
    movie_url = models.URLField(verify_exists = False, max_length = 250, blank = True)


class News(models.Model):
    """News on site"""
    name = models.CharField(max_length = 100, verbose_name = "News name")
    short_description = models.TextField(verbose_name = "Short description")
    full_description = models.TextField(verbose_name = "Full description")
    pub_date = models.DateTimeField(default = datetime.now)
    
    def __unicode__(self):
        return self.name 

    class Meta:
        ordering = ('-pub_date','name')
        verbose_name = "News-item "
        verbose_name_plural = "News on site"

    def get_absolute_url(self):
        return reverse('news_detail', args=[self.id])

models.signals.pre_save.connect(remove_imgs, sender = Episode)
models.signals.pre_save.connect(remove_imgs, sender = Serial )

