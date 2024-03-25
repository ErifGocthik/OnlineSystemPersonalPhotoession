from django.shortcuts import render
from django.views.generic import ListView

from photosessionapp.models import Photographer, CustomUser


def root_view(request):
    user = CustomUser
    return render(request, 'root.html', {'user': user})


class MainView(ListView):
    model = Photographer
    template_name = 'photosession/main.html'
    context_object_name = 'photographer'