from django.db import migrations


OFFICE_ADDRESS = (
    "Abuja Office: Suite D06 KENUJ O2 Mall , Opposite Summit Bible Church Kaura District\n\n"
    "Plot 1, Glory Land Community, after Emirate Hotel, Ajebamidele, Ado-Ekiti, Ekiti State"
)


def update_office_address(apps, schema_editor):
    SiteSetting = apps.get_model("core", "SiteSetting")
    SiteSetting.objects.update_or_create(
        name="head_office_address",
        defaults={"value": OFFICE_ADDRESS},
    )


def restore_empty_address(apps, schema_editor):
    SiteSetting = apps.get_model("core", "SiteSetting")
    SiteSetting.objects.filter(name="head_office_address").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(update_office_address, restore_empty_address),
    ]
