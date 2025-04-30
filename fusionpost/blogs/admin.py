from django.contrib import admin
from .models import TextPost


@admin.register(TextPost)
class TextPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish']
    list_filter = ['author', 'publish']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['publish']
    show_facets = admin.ShowFacets.ALWAYS