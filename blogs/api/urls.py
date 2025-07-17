from django.urls import path
from blogs import views

app_name = 'blogs_api'

urlpatterns = [
    path('post_list/', views.TextPostListView.as_view(), name='post_list'),
    path('post_detail/<int:post_id>', views.TextPostDetailView.as_view(), name='post_detail')
]

