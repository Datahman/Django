
# Generic views aka class based views
from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView, DeleteView,UpdateView
from django.urls import reverse_lazy


class HomepageView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums' # Context variable re assignment.

    def get_queryset(self):
        return Album.objects.all() # return query stores in variable object_list


class DetailpageView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


""" Model based form classes: CreateView, Edit object: UpdateView.."""

""" Create form based on the Album model """


class AddAlbum(CreateView):
    model = Album # Model to use
    fields = ['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model = Album # Model to use
    fields = ['artist','album_title','genre','album_logo']

"""Redirect to Home page upon sucessful deletion of an album object """
class DeleteAlbum(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')
    #
    # def get_success_url(self,**kwargs):
    #     if kwargs is None:
    #         return "Nada"
    #     else:
    #         return ('music:index', kwargs.keys())

    # def get_sucess_url(self,**kwargs):
    #     if kwargs is None:
    #
    #         return reverse('music:detail',args=(self.object.id,))
    #     else:
    #         return reverse('music:index', kwargs={'pk': kwargs['idnumber']})

#print(DeleteAlbum.__dict__.items())

