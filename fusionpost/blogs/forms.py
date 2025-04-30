from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TextPost

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': "Имя пользователя",
            "password1": "Пароль",
            "password2": "Повторите пароль",
            "email": "E-Mail"
            }


class TextPostForm(forms.ModelForm):
    class Meta:
        model = TextPost
        fields = ['title', 'body']
        widgets = {'body': forms.Textarea}
        labels = {"title": "Название", "body": "Текст"}