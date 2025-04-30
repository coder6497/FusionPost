from django.contrib import admin
from .models import TextPost


@admin.register(TextPost)
class TextPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish']
    list_filter = ['author', 'publish']
    date_hierarchy = 'publish'
    ordering = ['publish']
    show_facets = admin.ShowFacets.ALWAYS