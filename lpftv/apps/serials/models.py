from django.db import models
import Image, os

class Serial(models.Model):
    name = models.CharField(max_length = 50, verbose_name = "Serials' name")
    short_describe = models.TextField(verbose_name = "Short describe")
    full_describe = models.TextField(verbose_name = "Full describe")
    origin_img = models.ImageField(upload_to = "photos") 
    pub_date = models.DateTimeField()

    def save(self): 
         oldfile = self.origin_img.path
         models.Model.save(self)
         print oldfile + " : " + str(os.path.exists(oldfile))
         if os.path.exists(oldfile):
             print oldfile + " : " + os.path.exists(oldfile)
             os.remove(oldfile)
         oldfile = oldfile[:-4]+ "_small.jpeg"
         if os.path.exists(oldfile):
             os.remove(oldfile) 
         size = 128
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
    short_describe = models.TextField(verbose_name = "Shor describe")
    full_describe = models.TextField(verbose_name = "Full describe")
    origin_img = models.ImageField(upload_to = "photos")
    movie = models.FileField(upload_to = "serials")
    pub_date = models.DateTimeField()

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

class Comment(models.Model):
    author = models.CharField(max_length = 50, verbose_name = "Author")
    text = models.TextField(verbose_name = "Comment")
    link = models.ForeignKey(Movie)
    pub_date = models.DateTimeField("Comment's date")

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return author + ": " +links

