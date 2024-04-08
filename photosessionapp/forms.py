from django import forms
from django.forms import TextInput, ModelForm

from photosessionapp.models import Reservation, Photographer


class ReservationCreateForm(forms.ModelForm, forms.Form):
    class Meta:
        model = Reservation
        widgets = {
            'description': TextInput(attrs={'placeholder': 'Предпочтения'}),
        }
        exclude = ['id', 'email', 'status', 'photograph_id', 'phone_number']


class PhotographersCreateForm(forms.ModelForm, forms.Form):

    SHEDULE = [('Понедельник', "понедельник"), ("Вторник", "вторник"), ("Среда", "среда"),
            ("Четверг", "четверг"), ("Пятница", "пятница"), ('Суббота', "суббота"), ("Воскресенье", "воскресенье")]

    work_days = forms.MultipleChoiceField(
        choices=SHEDULE,
        initial='Понедельник',
        widget=forms.SelectMultiple(),
        required=True,
        label='Рабочие дни'
    )

    class Meta:
        model = Photographer
        exclude = ['id']


class PhotographerChangeForm(ModelForm):
    SHEDULE = [('Понедельник', "понедельник"), ("Вторник", "вторник"), ("Среда", "среда"),
               ("Четверг", "четверг"), ("Пятница", "пятница"), ('Суббота', "суббота"), ("Воскресенье", "воскресенье")]

    work_days = forms.MultipleChoiceField(
        choices=SHEDULE,
        initial='Понедельник',
        widget=forms.SelectMultiple(),
        required=True,
        label='Рабочие дни'
    )

    class Meta:
        model = Photographer
        exclude = ['id']