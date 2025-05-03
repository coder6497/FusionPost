from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_text_post/', views.create_text_post, name='create_text_post'),
    path('post_list/', views.post_list, name='post_list'),
    path('text_post_detail/<int:text_post_id>', views.text_post_detail, name='text_post_detail'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
    path('about_user/', views.about_user, name='about_user'),
    path('edit_user/', views.edit_user, name='edit_user')
]