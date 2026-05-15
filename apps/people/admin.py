from django.contrib import admin

from .models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "is_executive_director", "sort_order", "is_active")
    list_filter = ("is_executive_director", "is_active")
    list_editable = ("sort_order", "is_active")
    search_fields = ("name", "role", "bio")
    fieldsets = (
        (None, {"fields": ("name", "role", "bio")}),
        ("Photo", {"fields": ("photo", "photo_static_path")}),
        ("Executive Director", {"fields": ("is_executive_director", "vision", "message")}),
        ("Publishing", {"fields": ("sort_order", "is_active")}),
    )
