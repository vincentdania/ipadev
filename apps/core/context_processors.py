from .models import SiteSetting


def site_settings(request):
    values = {item.name: item.value for item in SiteSetting.objects.all()}
    return {"site_settings": values}
