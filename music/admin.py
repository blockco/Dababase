from django.contrib import admin

# Register your models here.
from .models import Album, song, dab

admin.site.register(Album)
admin.site.register(song)
admin.site.register(dab)