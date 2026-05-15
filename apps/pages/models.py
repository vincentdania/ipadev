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
