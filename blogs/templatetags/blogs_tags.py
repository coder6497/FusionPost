from django import template
from ..models import TextPost

register = template.Library()

@register.simple_tag
def image_name_without_path(post_id):
    return TextPost.objects.get(id=post_id).image.name.split('/')[-1]


@register.simple_tag
def get_image_size_in_megabytes(post_id):
    return round(TextPost.objects.get(id=post_id).image.size / (2 ** 10) ** 2, 2)