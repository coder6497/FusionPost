from .forms import TextPostForm, PhotoForGalleryForm
from .models import TextPost, PhotoForGallery

def get_params_for_createobject(request_post, request_files):
    return {
            "templates_by_post_type": {
                "text_post": "posts/create_text_post.html",
                "photo_gallery": "gallery/create_photo.html"
            },
            "forms_by_tags": {
                "text_post": [TextPostForm(request_post, request_files), TextPostForm()],
                "photo_gallery": [PhotoForGalleryForm(request_post, request_files), PhotoForGalleryForm()]
            },
            "headers": {
                "text_post": "Создать текстовый пост",
                "photo_gallery": "Галерея"
            }
        }

def get_params_for_getobject():
    return {"text_post": TextPost, "photo_gallery": PhotoForGallery}

def check_content_type_for_template(file_ext):
    return {
            'is_image': file_ext in ['.jpg', '.png', 'jpeg', '.bmp'],
            'is_video': file_ext in ['.mp4', '.mov', '.mkv', '.avi'],
            'is_audio': file_ext in ['.mp3', '.aac', '.wav']
    }

