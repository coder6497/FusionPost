from django.db import models
from django.conf import settings
from django.utils import timezone


class TextPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_text_posts')
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    body = models.CharField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish'])]
    
    def __str__(self):
        return self.title