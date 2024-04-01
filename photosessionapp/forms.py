from django import forms
from django.forms import TextInput

from photosessionapp.models import Reservation


class ReservationCreateForm(forms.ModelForm, forms.Form):
    class Meta:
        model = Reservation
        widgets = {
            'description': TextInput(attrs={'placeholder': 'Предпочтения'}),
            'phone_number': TextInput(attrs={'placeholder': '7(999) 999-99-99'})
        }
        exclude = ['id', 'email', 'status']