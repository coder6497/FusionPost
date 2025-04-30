from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class TextPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_text_posts')
    title = models.CharField(max_length=50)
    body = models.CharField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish'])]
    
    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.username