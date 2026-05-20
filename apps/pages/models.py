from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


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


class BlogPost(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"

    title = models.CharField(max_length=220)
    slug = models.SlugField(
        unique=True,
        blank=True,
        help_text="Leave blank to generate automatically from the title.",
    )
    excerpt = models.TextField(
        blank=True,
        help_text="Short summary shown on the blog listing page.",
    )
    body = models.TextField(help_text="Main blog content. Paragraph breaks are preserved.")
    featured_image = models.ImageField(upload_to="blog/", blank=True)
    featured_image_static_path = models.CharField(
        max_length=220,
        blank=True,
        help_text="Optional static image path for bundled blog images.",
    )
    author_name = models.CharField(max_length=120, default="IPADEV")
    published_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title) or "blog-post"
            slug = base_slug
            index = 2
            while BlogPost.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{index}"
                index += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

    @property
    def is_published(self):
        return self.status == self.Status.PUBLISHED and self.published_at <= timezone.now()


class BlogPostImage(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="gallery_images")
    caption = models.CharField(max_length=180, blank=True)
    alt_text = models.CharField(max_length=220, blank=True)
    image = models.ImageField(upload_to="blog/gallery/", blank=True)
    static_path = models.CharField(
        max_length=220,
        blank=True,
        help_text="Optional static image path for bundled blog gallery images.",
    )
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self):
        return self.caption or self.alt_text or f"Image for {self.post}"
