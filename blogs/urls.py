from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change_done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_change/', PasswordChangeView.as_view(success_url=reverse_lazy('blogs:password_change_done')), name='password_change'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_post/<str:post_type>', views.create_post, name='create_post'),
    path('post_list/', views.post_list, name='post_list'),
    path('post_detail/<int:post_id>/<str:post_type>', views.post_detail, name='post_detail'),
    path('delete_post/<int:post_id>/<str:post_type>', views.delete_post, name='delete_post'),
    path('about_user/', views.about_user, name='about_user'),
    path('edit_user/', views.edit_user, name='edit_user'),
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
    path('post_search/', views.search_posts, name='post_search')
]