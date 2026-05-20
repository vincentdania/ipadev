from django.db import migrations


OFFICE_ADDRESS = (
    "Abuja Office: Suite D06 KENUJ O2 Mall , Opposite Summit Bible Church Kaura District\n\n"
    "Ekiti Office: Plot 1, Glory Land Community, after Emirate Hotel, Ajebamidele, "
    "Ado-Ekiti, Ekiti State"
)


def update_office_address(apps, schema_editor):
    SiteSetting = apps.get_model("core", "SiteSetting")
    SiteSetting.objects.update_or_create(
        name="head_office_address",
        defaults={"value": OFFICE_ADDRESS},
    )


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_update_office_address"),
    ]

    operations = [
        migrations.RunPython(update_office_address, migrations.RunPython.noop),
    ]
