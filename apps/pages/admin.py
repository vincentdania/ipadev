from django.contrib import admin

from .models import AreaOfFocus, PageContent


@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ("key", "title", "is_published", "updated_at")
    list_filter = ("is_published",)
    search_fields = ("key", "title", "body")
    readonly_fields = ("updated_at",)
    fieldsets = (
        (
            "Editable website copy",
            {
                "fields": ("key", "title", "body", "image", "is_published"),
                "description": (
                    "Edit the title and body for the matching website section. Keep the key unchanged; "
                    "templates use it to place this content on the site."
                ),
            },
        ),
        ("System", {"fields": ("updated_at",)}),
    )


@admin.register(AreaOfFocus)
class AreaOfFocusAdmin(admin.ModelAdmin):
    list_display = ("title", "sort_order", "is_published")
    list_editable = ("sort_order", "is_published")
    search_fields = ("title", "description")
    fieldsets = (
        ("Focus area content", {"fields": ("title", "description", "icon_name")}),
        ("Publishing", {"fields": ("sort_order", "is_published")}),
    )
