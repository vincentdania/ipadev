from django.contrib import admin

from .models import AreaOfFocus, PageContent


@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ("key", "title", "is_published", "updated_at")
    list_filter = ("is_published",)
    search_fields = ("key", "title", "body")
    prepopulated_fields = {"key": ("title",)}


@admin.register(AreaOfFocus)
class AreaOfFocusAdmin(admin.ModelAdmin):
    list_display = ("title", "sort_order", "is_published")
    list_editable = ("sort_order", "is_published")
    search_fields = ("title", "description")
