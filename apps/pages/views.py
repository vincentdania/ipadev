from django.utils import timezone
from django.views.generic import DetailView, ListView, TemplateView

from apps.people.models import TeamMember

from .models import AreaOfFocus, BlogPost, ContentListItem, GalleryImage, PageContent

FOCUS_PILLARS = [
    {
        "icon": "female",
        "title": "Gender Equality and Women's Empowerment",
        "description": "Advancing the rights, participation, leadership, and socio-economic empowerment of women and girls.",
    },
    {
        "icon": "account_balance",
        "title": "Inclusive Governance and Active Citizenship",
        "description": "Promoting governance systems that are inclusive, participatory, transparent, and accountable to citizens.",
    },
    {
        "icon": "diversity_3",
        "title": "Social Justice and Inclusion",
        "description": "Promoting dignity, fairness, and respect for people facing social, economic, gender, or physical exclusion.",
    },
    {
        "icon": "school",
        "title": "Capacity Building and Institutional Strengthening",
        "description": "Supporting organizations, institutions, community structures, networks, and emerging leaders to strengthen effectiveness and resilience.",
    },
    {
        "icon": "eco",
        "title": "Sustainable Development and Community Resilience",
        "description": "Promoting locally driven approaches that improve livelihoods, strengthen resilience, and support long-term transformation.",
    },
]

def content_map():
    return {item.key: item for item in PageContent.objects.filter(is_published=True)}


def list_items(section):
    return ContentListItem.objects.filter(section=section, is_published=True)


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["content"] = content_map()
        context["areas"] = AreaOfFocus.objects.filter(is_published=True)[:4]
        context["pillars"] = FOCUS_PILLARS
        context["news_items"] = list_items("resource_items")[:3]
        context["executive_director"] = (
            TeamMember.objects.filter(is_active=True, is_executive_director=True).first()
        )
        return context


class AboutView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["content"] = content_map()
        context["values"] = list_items("about_values")
        return context


class AreasOfFocusView(TemplateView):
    template_name = "pages/areas_of_focus.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["content"] = content_map()
        context["areas"] = AreaOfFocus.objects.filter(is_published=True)
        context["pillars"] = FOCUS_PILLARS
        context["strategic_objectives"] = list_items("strategic_objectives")
        context["approaches"] = list_items("approaches")
        return context


class GetInvolvedView(TemplateView):
    template_name = "pages/get_involved.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["content"] = content_map()
        context["team_count"] = TeamMember.objects.filter(is_active=True).count()
        return context


class ImpactView(TemplateView):
    template_name = "pages/impact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["content"] = content_map()
        return context


class NewsView(TemplateView):
    template_name = "pages/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["content"] = content_map()
        context["news_items"] = list_items("resource_items")
        context["gallery_images"] = GalleryImage.objects.filter(is_published=True)
        return context


class BlogListView(ListView):
    model = BlogPost
    template_name = "pages/blog_list.html"
    context_object_name = "posts"
    paginate_by = 9

    def get_queryset(self):
        return BlogPost.objects.filter(
            status=BlogPost.Status.PUBLISHED,
            published_at__lte=timezone.now(),
        )


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "pages/blog_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return BlogPost.objects.filter(
            status=BlogPost.Status.PUBLISHED,
            published_at__lte=timezone.now(),
        )
