from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db.models import signals
from django.core.files.storage import default_storage
from django.dispatch import receiver


class TextPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_text_posts')
    image = models.ImageField(blank=True, upload_to='posts/%Y/%m/%d/')
    title = models.CharField(max_length=50)
    body = models.CharField(blank=True)
    publish = models.DateTimeField(default=timezone.now)
    private = models.BooleanField(default=False)

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
    

@receiver(signals.post_delete)
def delete_files_on_delete(sender, instance, **kwargs):
    file_fields = ['image', 'avatar']
    for field_name in file_fields:
        if hasattr(instance, field_name):
            file_field = getattr(instance, field_name)
            if file_field:
                default_storage.delete(file_field.name)