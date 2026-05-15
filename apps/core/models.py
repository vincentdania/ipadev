from django.db import models


class SiteSetting(models.Model):
    name = models.CharField(max_length=120, unique=True)
    value = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
