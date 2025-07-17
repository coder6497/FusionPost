from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include('blogs.urls', namespace='blogs')),
    path('', RedirectView.as_view(url='/blogs/', permanent=True)),
    path('api/', include('blogs.api.urls',  namespace='api'))
]