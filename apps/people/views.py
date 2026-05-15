from django.views.generic import TemplateView

from apps.pages.views import content_map

from .models import TeamMember


class TeamView(TemplateView):
    template_name = "people/team.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["executive_director"] = (
            TeamMember.objects.filter(is_active=True, is_executive_director=True).first()
        )
        context["board_members"] = TeamMember.objects.filter(
            is_active=True, is_executive_director=False
        )
        context["content"] = content_map()
        return context
