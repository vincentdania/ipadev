from rest_framework import serializers, viewsets

from .models import AreaOfFocus, PageContent


class PageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContent
        fields = ["id", "key", "title", "body", "image", "updated_at"]


class AreaOfFocusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaOfFocus
        fields = ["id", "title", "description", "icon_name", "sort_order"]


class PageContentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PageContentSerializer
    queryset = PageContent.objects.filter(is_published=True)
    lookup_field = "key"


class AreaOfFocusViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AreaOfFocusSerializer
    queryset = AreaOfFocus.objects.filter(is_published=True)
