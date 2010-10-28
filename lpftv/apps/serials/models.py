from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
import Image, os

__docformat__ = "restructuredtext"

class CFilm(models.Model):
    """
    Base model for 'Movie' and 'Serial' models 
    """
    name = models.CharField(max_length = 50, verbose_name = "Serials' name")
    full_description = models.TextField(verbose_name = "Full description", blank = True)
    origin_img = models.ImageField(upload_to = "photos") 
    last_img = models.ImageField(upload_to = "photos", editable = False, default = "")
    pub_date = models.DateTimeField()

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


    def pre_save(self):
        """Remove old images"""
        try: 
            if os.path.exists(self.get_last_img_path()):
                os.remove(self.get_last_img_path())
            if os.path.exists(self.last_img.path):
                os.remove(self.last_img.path)
        except: pass 
        self.last_img = self.origin_img

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


def pre_save(sender, **kwargs):
    """Call 'pre_save()' to all objects what saving"""
    sobject = kwargs['instance']
    try:
        sobject.pre_save()
    except:
        None

class Serial(CFilm):
    """Contein serial description and movie"""
    short_description = models.TextField(verbose_name = "Short description")

    def get_absolute_url(self):
        return reverse('serial_detail', args=[self.id])

class Movie(CFilm):
    """This model is for save real movie(serial)"""
    serial = models.ForeignKey(Serial)
    movie = models.FileField(upload_to = "serials")

    def get_absolute_url(self):
        """Url for download"""
        return self.movie.url

class NewsRecord(models.Model):
    """This models uses for save news"""
    name = models.CharField(max_length = 100, verbose_name = "News name")
    short_description = models.TextField(verbose_name = "Short description")
    full_description = models.TextField(verbose_name = "Full desribe")
    pub_date = models.DateTimeField()
    
    def __unicode__(self):
        return self.name 

    class Meta:
        ordering = ('-pub_date','name')

    def get_absolute_url(self):
        return reverse('news_detail', args=[self.id])

models.signals.pre_save.connect(pre_save)

