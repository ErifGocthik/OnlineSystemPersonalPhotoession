from django.urls import path

from authapp.views import PhotographerChangeView
from photosessionapp.views import MainView, PhotographerListView, ReservationCreateView, GetAnswer, \
    PhotographerCreateView, PhotographerDetailView, gallery_view

app_name = 'photosessionapp'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('photographer/', PhotographerListView.as_view(), name='photographer'),
    path('reservation/<int:pk>/', ReservationCreateView.as_view(), name='reservation'),
    path('setanswer/<int:pk>/', GetAnswer.as_view(), name='setanswer'),
    path('photographerform/', PhotographerCreateView.as_view(), name='photographerform'),
    path('photographer-profile/<int:pk>/', PhotographerDetailView.as_view(), name='photo-profile'),
    path('photographer-change/<int:pk>/', PhotographerChangeView.as_view(), name='change-profile'),
    path('gallery/', gallery_view, name='gallery')
]