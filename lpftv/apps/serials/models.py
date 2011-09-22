# -*- coding: utf-8 -*-
import logging
from datetime import datetime
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
import Image, os

# Get an instance of a logger
logger = logging.getLogger(__name__)
CROP_EXP = '.crop'
SMALL_EXP = '.small'


__docformat__ = "restructuredtext"

class CFilm(models.Model):
    """
    Base model for 'Episode' and 'Serial' models 
    """
    name = models.CharField(max_length = 50, verbose_name = "name")
    full_description = models.TextField(verbose_name = "Full description", blank = True)
    origin_img = models.ImageField(upload_to = "photos/", blank = True) 
    pub_date = models.DateTimeField(default = datetime.now)

    def get_thumb_url(self, exp = SMALL_EXP):
        """Return url to small image(if not small image return default)"""
        if self.origin_img:
            return self.origin_img.url[:self.origin_img.url.rindex('.')]+ \
                exp+self.origin_img.url[self.origin_img.url.rindex('.'):]
        else:
            return settings.IMAGE_DEFAULT

    def get_thumb_path(self, exp = SMALL_EXP):
        """Return path in local disk to small image"""
        return self.origin_img.path[:self.origin_img.path.rindex('.')]+ \
            exp+self.origin_img.path[self.origin_img.path.rindex('.'):]

    def get_image_url(self):
        """Return image url or default image url"""
        if self.origin_img:
            return self.origin_img.url
        else:
            return settings.IMAGE_DEFAULT

    def save_thumbs(self):
    #Save both cropped and scaled image
        im_path = self.origin_img.path
        if im_path and os.path.exists(im_path):
            try:
                im = Image.open(im_path)

                offset = im.size[0] - im.size[1]
                offset /= 2
                if offset > 0:
                    box = (offset, 0, im.size[0]-offset, im.size[1])
                if offset < 0:
                    offset *= -1
                    box = (0, offset, im.size[0], im.size[1]-offset)
                im_crop = im.crop(box)
                im_crop.thumbnail((settings.IMAGE_XY, settings.IMAGE_XY), Image.ANTIALIAS)
                im_crop.save(self.get_thumb_path(CROP_EXP), "jpeg") 

                im.thumbnail((settings.SERIAL_IMAGE_XY,settings.SERIAL_IMAGE_XY),
                    Image.ANTIALIAS)
                im.save(self.get_thumb_path(SMALL_EXP), "jpeg") 
            except IOError:
                logger.error("Can't get small image!")

    def save(self, *args, **kwargs):
        """Saving small image 'size'x'size' in local disk"""
        super(CFilm, self).save(*args, **kwargs)
        if self.origin_img:
            self.save_thumbs()


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
        ordering = ('pub_date',)
        abstract = True

class Serial(CFilm):
    """Contains serial description and movie"""
    short_description = models.TextField(verbose_name = "Short description")
    slug = models.SlugField(max_length = 250, unique = True)
    last_modified = models.DateTimeField(auto_now_add = True, editable = True)
    class Meta:
        ordering = ('-last_modified',)
               

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
                CROP_EXP+self.origin_img.url[self.origin_img.url.rindex('.'):]
        else:
            return self.serial.get_thumb_url(CROP_EXP)

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
    image = models.ImageField(upload_to = "banner", blank = False,  help_text ="Image size should be - 950 x 335")
    to_url = models.URLField(verify_exists = False, max_length = 250, blank = True)
    priority = models.IntegerField(default = "0", help_text = "Images sorted by priority")

    def __unicode__(self):
        return "%s - %s" % (self.to_url, self.title)

    class Meta:
        ordering = ('priority',)
        verbose_name = "Rotation image"
        verbose_name_plural = "Rotation images"


def modify(sender, instance, *args, **kwargs):
    """change ordering of serials"""
    instance.serial.last_modified = datetime.now()
    instance.serial.save()

models.signals.pre_save.connect(modify, sender = Episode)
