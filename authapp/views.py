from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from authapp.forms import CustomUserCreateForm
from photosessionapp.models import CustomUser


class UserCreationView(CreateView):
    model = CustomUser
    template_name = 'sign-up.html'
    form_class = CustomUserCreateForm


    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.password = make_password(user.password)
        user.save()
        return redirect(reverse_lazy('auth:login'))


class UserView(DetailView):
    model = CustomUser
    template_name = 'profile.html'
    context_object_name = 'user'

    def get_context_data(self, pk: int):
        this_user = get_object_or_404(CustomUser, pk=pk)
        profile_user = self.request.user.pk
        return {'this_user': this_user, 'profile_user': profile_user}

    def get(self, request, pk: int, *args, **kwargs):
        if request.user.pk != self.get_context_data(pk).get('profile_user'):
            return redirect(reverse_lazy('main:main'))
        return render(self.request, self.template_name, self.get_context_data(pk))

def user_logout(request):
    if request.user:
        logout(request)
    return redirect(reverse_lazy('main:main'))