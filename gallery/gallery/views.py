from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from .models import Photo

# Create your views here.

def home(request):
    return render(request, 'home.html')

class PhotoListView(ListView):
    model = Photo
    template_name = "photo_list.html"
    context_object_name = "photos"

class PhotoDetailView(DetailView):
    model = Photo
    template_name = "photo_detail.html"
    context_object_name = "photo"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['datetime_added'] = self.object.created_at.strftime('%b %d, %Y %I:%M %p')
        return context

def my_view(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    url = reverse('photo_detail', kwargs={'pk': photo.pk})
    return redirect(url)

