from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import TextPost, CustomUser, Comment, PhotoForGallery


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput())
    password = forms.CharField(label="Пароль",widget=forms.PasswordInput())
    error_messages = {"invalid_login": "Неверное имя поьзователя или пароль. Повторите попытку"}

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Текущий пароль", widget=forms.PasswordInput())
    new_password1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput())
    new_password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput())
    error_messages = {"password_incorrect": "Текущий пароль введен неверно",
                      "password_mismatch": "Новые пароли не совпадают",
                      "password_too_short": "Пароль слишком короткий",
                      "password_common": "Пароль слишком простой"
                    }


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(), help_text="До 150 символов включительно")
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput())

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
            "phone": "Номер телефона",
            "avatar": "Аватар"
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'body']
        labels = {"title": "Название", "body": "Текст"}
    

class PhotoForGalleryForm(forms.ModelForm):
    class Meta:
        model = PhotoForGallery
        fields = ['image']
        labels = {'image': 'Загрузить фотографию 📷'}

class SearchForm(forms.Form):
    query = forms.CharField()