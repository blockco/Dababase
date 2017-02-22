from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from .models import Album, song, dab
from .forms import DabModelForm

# Create your views here.

class DabListView(ListView):
    template_name = "music/dab_list.html"
    context_object_name = "all_dabs"
    
    def get_queryset(self):
        return dab.objects.order_by("timestamp")[:20]
        
class DabCreateView(CreateView):
    form_class = DabModelForm
    template_name = 'music/dab_create.html'
# def index(request):
#     all_dabs = dab.objects.all()
#     return render(request, 'music/index.html', {'all_dabs': all_dabs})

# def detail(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     return render(request, 'music/detail.html', {'album': album})
#     # try:
#     #     album = Album.objects.get(pk=album_id)
#     # except Album.DoesNotExist:
#     #     raise Http404("Album does not exist")
    
# def favorite(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song = album_id.song_set(pk=request.POST['song'])
#     except (KeyError, song.DoesNotExist):
#         return render(request, 'music/index.html', {
#             'all_albums': all_albums,
#             'error_message': "You did not select a valid song",
#         })
#     else:
#         selected_song.is_favorite = True
#         selected_song.save();
#         return render(request, 'music/index.html', {'all_albums': all_albums})