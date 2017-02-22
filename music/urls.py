from django.conf.urls import url
from .views import DabListView, DabCreateView

app_name = 'music'

urlpatterns = [
    # /music/
    
    url(r'^create/$', DabCreateView.as_view(), name='create'),
    url(r'^$', DabListView.as_view(), name='index'),
    
    #/music/<album_id>
    #url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    
    # #/music/<album_id>/favorite
    # url(r'^(?P<album_id>[0-9]+)/$', views.favorite, name='favorite'),
]
