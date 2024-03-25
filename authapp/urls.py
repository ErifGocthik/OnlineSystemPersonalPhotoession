from django.contrib.auth.views import LoginView
from django.urls import path, reverse_lazy
from django.views.generic import CreateView

from authapp.forms import CustomUserCreateForm
from authapp.views import UserCreationView, user_logout, UserView

app_name = 'customapp'

urlpatterns = [
    path('sign-in/', LoginView.as_view(template_name='sign-in.html', next_page=reverse_lazy('main:main')), name='login'),
    path('sign-up/', UserCreationView.as_view(), name='authorization'),
    path('logout/', user_logout, name='logout'),
    path('profile/<int:pk>', UserView.as_view(), name='profile')
]