from django.db import models
from django.urls import reverse


class PageContent(models.Model):
    key = models.SlugField(unique=True)
    title = models.CharField(max_length=180)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to="pages/", blank=True)
    is_published = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["key"]

    def __str__(self):
        return self.title


class AreaOfFocus(models.Model):
    title = models.CharField(max_length=160)
    description = models.TextField()
    icon_name = models.CharField(max_length=80, blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "title"]
        verbose_name_plural = "areas of focus"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("areas_of_focus")


class ContentListItem(models.Model):
    section = models.SlugField(
        help_text="Groups this item for a website section, for example about_values or resource_items.",
    )
    eyebrow = models.CharField(
        max_length=120,
        blank=True,
        help_text="Optional small label shown above the title, such as Focus Area or Gender Equality.",
    )
    title = models.CharField(max_length=180)
    body = models.TextField(blank=True)
    icon_name = models.CharField(
        max_length=80,
        blank=True,
        help_text="Optional Material Symbols icon name.",
    )
    sort_order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["section", "sort_order", "title"]

    def __str__(self):
        return f"{self.section}: {self.title}"


class GalleryImage(models.Model):
    title = models.CharField(max_length=160)
    caption = models.CharField(max_length=180, blank=True)
    alt_text = models.CharField(max_length=220, blank=True)
    image = models.ImageField(upload_to="gallery/", blank=True)
    static_path = models.CharField(
        max_length=180,
        blank=True,
        help_text="Optional static image path, for bundled launch/gallery images.",
    )
    sort_order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "title"]

    def __str__(self):
        return self.title
