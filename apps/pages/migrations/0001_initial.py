from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AreaOfFocus",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=160)),
                ("description", models.TextField()),
                ("icon_name", models.CharField(blank=True, max_length=80)),
                ("sort_order", models.PositiveIntegerField(default=0)),
                ("is_published", models.BooleanField(default=True)),
            ],
            options={"verbose_name_plural": "areas of focus", "ordering": ["sort_order", "title"]},
        ),
        migrations.CreateModel(
            name="PageContent",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("key", models.SlugField(unique=True)),
                ("title", models.CharField(max_length=180)),
                ("body", models.TextField(blank=True)),
                ("image", models.ImageField(blank=True, upload_to="pages/")),
                ("is_published", models.BooleanField(default=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["key"]},
        ),
    ]
