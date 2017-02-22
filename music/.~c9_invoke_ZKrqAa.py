from django.conf.urls import url
from .v import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'/mui^$', views.index, name='index'),
    
    #/music/<album_id>
    #url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    
    # #/music/<album_id>/favorite
    # url(r'^(?P<album_id>[0-9]+)/$', views.favorite, name='favorite'),
]
