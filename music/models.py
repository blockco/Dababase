from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from datetime import timedelta, datetime, date
from django.utils import timezone

from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.album_title + ' - ' + self.artist

class song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favortie = models.BooleanField(default=False)
    
    def __str__(self):
        return self.song_title
        
class dab(models.Model):
    handle = models.CharField(max_length=250)
    size = models.CharField(max_length=250)
    timestamp = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.handle
    
    def get_absolute_url(self):
        return reverse("music:index")