from django.urls import path
from blogs import views

app_name = 'blogs_api'

urlpatterns = [
    path('post_list/', views.TextPostListView.as_view(), name='post_list')
]

