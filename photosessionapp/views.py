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

    def get_context_data(self, *, object_list=None, **kwargs):
        photographers = Photographer.objects.all()[:3]
        return {'photographer': photographers}

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.get_context_data())


class PhotographerListView(ListView):
    paginate_by = 4
    model = Photographer
    context_object_name = 'photographer'
    template_name = 'photosession/photographer.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        photographers = Photographer.objects.all()
        count = photographers.count()
        return {'count': count}

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.get_context_data())
