from django.urls import path

from photosessionapp.views import MainView, PhotographerListView, ReservationCreateView

app_name = 'photosessionapp'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('photographer/', PhotographerListView.as_view(), name='photographer'),
    path('reservation/', ReservationCreateView.as_view(), name='reservation')
]