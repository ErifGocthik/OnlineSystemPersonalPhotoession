from django.urls import path

from photosessionapp.views import MainView

app_name = 'photosessionapp'

urlpatterns = [
    path('', MainView.as_view(), name='main')
]