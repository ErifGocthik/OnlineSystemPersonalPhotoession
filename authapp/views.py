from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from django.forms import ModelForm
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView

from authapp.forms import CustomUserCreateForm, PhotographerCreateForm
from photosessionapp.forms import PhotographerChangeForm
from photosessionapp.models import CustomUser, Photographer, Reservation


def set_photographer(user):
    if user.user_type == '2':
        customuser = CustomUser.object.get(id=user.pk)
        photo = Photographer.objects.create(user_id=customuser)
        photo.save()
    return redirect(reverse_lazy('auth:login'))

class UserCreationView(CreateView):
    model = CustomUser
    template_name = 'sign-up.html'
    form_class = CustomUserCreateForm

    def get_context_data(self, **kwargs):
        form = self.form_class()
        return {'form': form}

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.password = make_password(user.password)
        user.save()
        set_photographer(user)
        return redirect(reverse_lazy('auth:login'))


class UserView(DetailView):
    model = CustomUser
    template_name = 'profile.html'
    context_object_name = 'user'

    def get_context_data(self, pk: int):
        profile_user = self.request.user.pk
        photographer_profile = Photographer.objects.get(user_id=self.request.user)
        self_reservations = Reservation.objects.filter(email=self.request.user.email)
        reservation = Reservation.objects.filter(photograph_id__user_id =self.request.user)
        return {'profile_user': profile_user, 'reservation': reservation, 'self_reservation': self_reservations,
                'photographer_profile': photographer_profile}

    def get(self, request, pk: int, *args, **kwargs):
        if request.user.pk != self.get_context_data(pk).get('profile_user'):
            return redirect(reverse_lazy('main:main'))
        return render(self.request, self.template_name, self.get_context_data(pk))

    # def post(self):

class PhotographerChangeView(DetailView):
    model = Photographer
    context_object_name = 'photographer'
    template_name = 'photographer-change-form.html'

    def get_context_data(self, pk: int, **kwargs):
        model = get_object_or_404(Photographer, pk=pk)
        form = PhotographerChangeForm(instance=model)
        return {'form': form, 'model': model}

    def get(self, request, pk: int, *args, **kwargs):
        return render(self.request, self.template_name, self.get_context_data(pk))

    def post(self, request, pk:int):
        form = PhotographerChangeForm(self.request.POST, instance=self.get_context_data(pk).get('model'))
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid()

    def form_valid(self, form):
        form.save()
        return redirect(reverse_lazy('auth:profile', kwargs = {'pk': self.request.user.pk}))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
def user_logout(request):
    if request.user:
        logout(request)
    return redirect(reverse_lazy('main:main'))