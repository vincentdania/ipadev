from rest_framework import serializers, viewsets

from .models import TeamMember


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = [
            "id",
            "name",
            "role",
            "bio",
            "photo",
            "photo_static_path",
            "is_executive_director",
            "vision",
            "message",
            "sort_order",
        ]


class TeamMemberViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TeamMemberSerializer
    queryset = TeamMember.objects.filter(is_active=True)
