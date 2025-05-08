from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import TextPost, CustomUser, Comment

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'password1', 'password2', 'avatar']
        labels = {
            'username': "Имя пользователя",
            "first_name": "Имя",
            "last_name": "Фамилия",
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


class EditUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'avatar']
        labels = {
            "username": "Имя пользователя",
            "first_name": "Имя",
            "last_name": "Фамилия",
            "email": "E-Mail",
            "phone": "Номер телефона"
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'body']
        labels = {"title": "Название", "body": "Текст"}
    
class SearchForm(forms.Form):
    query = forms.CharField()
