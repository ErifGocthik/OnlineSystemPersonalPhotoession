from django import forms
from django.forms import TextInput

from photosessionapp.models import CustomUser


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
            'email': TextInput(attrs={'placeholder': 'Эл. почта'}),
        }
        fields = ['username', 'name', 'surname', 'email', 'user_type', 'password', 'password_repeat', 'agreement']

# class LoginUserView(forms.Form):
