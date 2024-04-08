from django import forms
from django.forms import TextInput

from photosessionapp.models import CustomUser, Photographer


class CustomUserCreateForm(forms.ModelForm, forms.Form):
    agreement = forms.BooleanField(label='Соглашение')
    password = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'form-control'}))
    password_repeat = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'placeholder': 'Подтверждениие пароля', 'class': 'form-control'}))
    class Meta:
        model = CustomUser
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Имя Пользователя'}),
            'name': TextInput(attrs={'placeholder': 'Имя'}),
            'surname': TextInput(attrs={'placeholder': 'Фамилия'}),
            'phone_number': TextInput(attrs={'placeholder': 'Номер Телефона'}),
            'email': TextInput(attrs={'placeholder': 'Эл. почта'}),
        }
        fields = ['username', 'name', 'surname', 'phone_number', 'email', 'user_type', 'password', 'password_repeat', 'agreement']


class PhotographerCreateForm(forms.ModelForm):
    class Meta:
        model = Photographer
        fields = ['user_id', 'photo', 'bio', 'tech']