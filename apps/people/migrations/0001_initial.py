from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TeamMember",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=160)),
                ("role", models.CharField(max_length=180)),
                ("bio", models.TextField(blank=True)),
                ("photo", models.ImageField(blank=True, upload_to="team/")),
                (
                    "photo_static_path",
                    models.CharField(
                        blank=True,
                        help_text="Optional static image path, for migrated legacy assets such as img/name.jpeg.",
                        max_length=180,
                    ),
                ),
                ("is_executive_director", models.BooleanField(default=False)),
                ("vision", models.TextField(blank=True)),
                ("message", models.TextField(blank=True)),
                ("sort_order", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={"ordering": ["sort_order", "name"]},
        ),
    ]
