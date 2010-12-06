# -*- coding: utf-8 -*-
import logging
from datetime import datetime
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
import Image, os

# Get an instance of a logger
logger = logging.getLogger(__name__)



__docformat__ = "restructuredtext"

class CFilm(models.Model):
    """
    Base model for 'Episode' and 'Serial' models 
    """
    name = models.CharField(max_length = 50, verbose_name = "name")
    full_description = models.TextField(verbose_name = "Full description", blank = True)
    origin_img = models.ImageField(upload_to = "photos/", blank = True) 
    last_img = models.ImageField(upload_to = "photos/", editable = False, blank = True, default = "")
    pub_date = models.DateTimeField(default = datetime.now)

    def get_thumb_url(self, exp = ".small"):
        """Return url to small image(if not small image return default)"""
        if self.origin_img:
            return self.origin_img.url[:self.origin_img.url.rindex('.')]+ \
                exp+self.origin_img.url[self.origin_img.url.rindex('.'):]
        else:
            return settings.IMAGE_DEFAULT

    def get_thumb_path(self, exp = ".small"):
        """Return path in local disk to small image"""
        return self.origin_img.path[:self.origin_img.path.rindex('.')]+ \
            exp+self.origin_img.path[self.origin_img.path.rindex('.'):]

    def get_last_img_path(self, exp = ".small"):
        """This function used only in pre_save()"""
        if self.last_img:
            return self.last_img.path[:self.last_img.path.rindex('.')]+ \
                exp+self.last_img.path[self.last_img.path.rindex('.'):]
        else: "" 

    def get_image_url(self):
        """Return image url or default image url"""
        if self.origin_img:
            return self.origin_img.url
        else:
            return settings.IMAGE_DEFAULT

    def save_thumb(self, size, crop, im_path, tm_path):
        if im_path:
            try:
                im = Image.open(im_path)
                if crop:
                    offset = im.size[0] - im.size[1]
                    offset /= 2
                    if offset > 0:
                        box = (offset, 0, im.size[0]-offset, im.size[1])
                    if offset < 0:
                        offset *= -1
                        box = (0, offset, im.size[0], im.size[1]-offset)
                    im = im.crop(box)
                im.thumbnail((size, size), Image.ANTIALIAS)
                im.save(tm_path, "jpeg") 
            except IOError:
                logger.error("Can't get small image!")

    def save(self, crop = False, size = settings.IMAGE_XY):
        """Saving small image 'size'x'size' in local disk"""
        super(CFilm, self).save()
        if self.origin_img:
            im_path = self.origin_img.path
            tm_path = self.get_thumb_path()
            self.save_thumb(size, crop, im_path, tm_path)


    def delete(self):
        """Remove images and remove record in database"""
        try:
            if self.origin_img:
                if os.path.exists(self.origin_img.path):
                    os.remove(self.origin_img.path)
                if os.path.exists(self.get_thumb_path()):
                    os.remove(self.get_thumb_path())
        except IOError: 
            logger.error("Can't remove file")

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('-pub_date',)
        abstract = True


def remove_imgs(sender, instance, *args, **kwargs):
    """Remove old images"""
    if instance:
        try: 
            if os.path.exists(instance.get_last_img_path()):
                os.remove(instance.get_last_img_path())
            if os.path.exists(instance.last_img.path):
                os.remove(instance.last_img.path)
        except: 
            logger.error("Can't remove old image")
        instance.last_img = instance.origin_img


class Serial(CFilm):
    """Contains serial description and movie"""
    short_description = models.TextField(verbose_name = "Short description")
    slug = models.SlugField(max_length = 250, unique = True)
    def save(self):
        super(Serial, self).save(crop = False)
        if self.origin_img and os.path.exists(self.origin_img.path): 
             im_path = self.origin_img.path
             tm_path = self.get_thumb_path(exp = ".crop")
             crop = True
             size = settings.IMAGE_XY
             self.save_thumb(size, crop, im_path, tm_path)
               

    def get_absolute_url(self):
        return reverse('serial_detail', args=[self.slug])

class Episode(CFilm):
    """This model is for episode"""
    serial = models.ForeignKey(Serial)
    download_url = models.URLField(verify_exists = False, max_length = 250, blank = True)
    watch_online_url = models.URLField(verify_exists = False, max_length = 250, blank = True)

    def __unicode__(self):
        return "%s - %s" % (self.serial.name, self.name)

    def get_image_url(self):
        """Return image url or default image url"""
        if self.origin_img:
            return self.origin_img.url
        else:
            return self.serial.get_image_url()

    def get_thumb_url(self):
        """Return url to small image(if not small image return default)"""
        if self.origin_img:
            return self.origin_img.url[:self.origin_img.url.rindex('.')]+ \
                ".small"+self.origin_img.url[self.origin_img.url.rindex('.'):]
        else:
            return self.serial.get_thumb_url(".crop")

    def get_absolute_url(self):
        return reverse('episode_detail', args=[self.serial.slug, self.id])


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

class RImage(models.Model):
    """
    Rotion images
    """
    title = models.CharField(max_length = 50, verbose_name = "title")
    image = models.ImageField(upload_to = "baner", blank = False)
    to_url = models.URLField(verify_exists = False, max_length = 250, blank = True)

    def __unicode__(self):
        return "%s - %s" % (self.to_url, self.title)

models.signals.pre_save.connect(remove_imgs, sender = Episode)
models.signals.pre_save.connect(remove_imgs, sender = Serial )
