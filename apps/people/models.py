from django.db import models


class TeamMember(models.Model):
    name = models.CharField(max_length=160)
    role = models.CharField(max_length=180)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="team/", blank=True)
    photo_static_path = models.CharField(
        max_length=180,
        blank=True,
        help_text="Optional static image path, for migrated legacy assets such as img/name.jpeg.",
    )
    is_executive_director = models.BooleanField(default=False)
    vision = models.TextField(blank=True)
    message = models.TextField(blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name
