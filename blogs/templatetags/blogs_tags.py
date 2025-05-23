from django import template
from ..parameters import get_params_for_getobject
from django.core.files.images import get_image_dimensions  

register = template.Library()
get_params = get_params_for_getobject()

@register.simple_tag
def image_name_without_path(post_id, post_type):
    return get_params[post_type].objects.get(id=post_id).image.name.split('/')[-1]


@register.simple_tag
def get_image_size_in_megabytes(post_id, post_type):
    return round(get_params[post_type].objects.get(id=post_id).image.size / (2 ** 10) ** 2, 2)

@register.simple_tag
def get_image_width_height(post_id, post_type):
    obj = get_params[post_type].objects.get(id=post_id)
    width, height = get_image_dimensions(obj.image)
    return f"{width}x{height}"
