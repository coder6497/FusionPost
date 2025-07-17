from rest_framework import serializers
from blogs.models import TextPost

class TextPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextPost
        fields = ['id', 'author', 'title', 'body', 'publish', 'private']
