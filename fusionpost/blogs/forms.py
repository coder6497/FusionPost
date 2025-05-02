from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import TextPost, CustomUser

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'password1', 'password2', 'avatar']
        labels = {
            'username': "Имя пользователя",
            "password1": "Пароль",
            "password2": "Повторите пароль",
            "email": "E-Mail"
            }


class TextPostForm(forms.ModelForm):
    class Meta:
        model = TextPost
        fields = ['image', 'title', 'body', 'private']
        widgets = {'body': forms.Textarea}
        labels = {"title": "Название", "body": "Текст", "Изображение": "image", "Приватный": "private"}


