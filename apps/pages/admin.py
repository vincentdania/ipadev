from django.contrib import admin

from .models import AreaOfFocus, BlogPost, BlogPostImage, ContentListItem, GalleryImage, PageContent


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


@admin.register(ContentListItem)
class ContentListItemAdmin(admin.ModelAdmin):
    list_display = ("section", "title", "eyebrow", "sort_order", "is_published")
    list_filter = ("section", "is_published")
    list_editable = ("sort_order", "is_published")
    search_fields = ("section", "eyebrow", "title", "body", "icon_name")
    fieldsets = (
        (
            "Website list item",
            {
                "fields": ("section", "eyebrow", "title", "body", "icon_name"),
                "description": (
                    "Use section to place this item in the matching repeatable website area. "
                    "Common sections include about_values, strategic_objectives, approaches, "
                    "and resource_items."
                ),
            },
        ),
        ("Publishing", {"fields": ("sort_order", "is_published")}),
    )


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "caption", "sort_order", "is_published")
    list_filter = ("is_published",)
    list_editable = ("sort_order", "is_published")
    search_fields = ("title", "caption", "alt_text", "static_path")
    fieldsets = (
        ("Image content", {"fields": ("title", "caption", "alt_text", "image", "static_path")}),
        ("Publishing", {"fields": ("sort_order", "is_published")}),
    )


class BlogPostImageInline(admin.TabularInline):
    model = BlogPostImage
    extra = 1
    fields = ("caption", "alt_text", "image", "static_path", "sort_order")


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    inlines = (BlogPostImageInline,)
    list_display = ("title", "author_name", "status", "published_at", "updated_at")
    list_filter = ("status", "published_at", "author_name")
    search_fields = ("title", "excerpt", "body", "author_name")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "published_at"
    fieldsets = (
        (
            "Blog post",
            {
                "fields": (
                    "title",
                    "slug",
                    "excerpt",
                    "body",
                    "featured_image",
                    "featured_image_static_path",
                    "author_name",
                )
            },
        ),
        ("Publishing", {"fields": ("status", "published_at")}),
        ("System", {"fields": ("created_at", "updated_at")}),
    )
