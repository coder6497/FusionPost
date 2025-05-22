from django.contrib import admin
from .models import TextPost, CustomUser, Comment, PhotoForGallery


@admin.register(TextPost)
class TextPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish']
    list_filter = ['author', 'publish']
    date_hierarchy = 'publish'
    ordering = ['publish']
    show_facets = admin.ShowFacets.ALWAYS


@admin.register(CustomUser)
class CustomModelAdmin(admin.ModelAdmin):
    list_display =  ['username', 'email', 'phone']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'title', 'body', 'publish']
    list_filter = ['author', 'publish']
    date_hierarchy = 'publish'
    ordering = ['publish']
    show_facets = admin.ShowFacets.ALWAYS


@admin.register(PhotoForGallery)
class PhotoForGalleryAdmin(admin.ModelAdmin):
    list_display = ['photo', 'author', 'publish']
    list_filter = ['author', 'publish']
    date_hierarchy = 'publish'
    ordering = ['publish']
    show_facets = admin.ShowFacets.ALWAYS