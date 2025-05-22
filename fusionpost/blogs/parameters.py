from .forms import TextPostForm, PhotoForGalleryForm


def get_params(request_post, request_files):
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