from django.views.generic import TemplateView

from apps.people.models import TeamMember

from .models import AreaOfFocus, PageContent

STRATEGIC_OBJECTIVES = [
    "Promote inclusion and equitable access to opportunities.",
    "Strengthen institutions and community systems.",
    "Advance gender equality and social justice.",
    "Support leadership and capacity development.",
    "Encourage citizen participation and accountability.",
    "Foster innovation and sustainable development solutions.",
    "Deliver measurable and lasting impact within communities.",
]

APPROACHES = [
    "Policy advocacy and systems engagement",
    "Community mobilization and citizen engagement",
    "Capacity strengthening and leadership development",
    "Strategic partnerships and collaboration",
    "Research, learning, and evidence generation",
    "Inclusive programme design and implementation",
    "Accountability and sustainable impact",
]

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

NEWS_ITEMS = [
    {
        "category": "Focus Area",
        "date": "Gender Equality",
        "title": "Women's leadership and political participation",
        "summary": "IPADEV supports leadership development, mentorship, and gender-responsive systems that strengthen women's voices in decision-making spaces.",
        "icon": "female",
    },
    {
        "category": "Focus Area",
        "date": "Active Citizenship",
        "title": "Civic education and citizen engagement",
        "summary": "The organization promotes public dialogue, stakeholder engagement, citizen feedback mechanisms, and democratic participation.",
        "icon": "campaign",
    },
    {
        "category": "Focus Area",
        "date": "Institutional Strengthening",
        "title": "Capacity building and organizational resilience",
        "summary": "IPADEV provides practical support for leadership systems, programme effectiveness, accountability, and long-term sustainability.",
        "icon": "hub",
    },
]

def content_map():
    return {item.key: item for item in PageContent.objects.filter(is_published=True)}


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["content"] = content_map()
        context["areas"] = AreaOfFocus.objects.filter(is_published=True)[:4]
        context["pillars"] = FOCUS_PILLARS
        context["news_items"] = NEWS_ITEMS
        context["executive_director"] = (
            TeamMember.objects.filter(is_active=True, is_executive_director=True).first()
        )
        context["quote"] = (
            "Societies thrive when every individual, regardless of gender, social status, "
            "disability, age, or background, has a fair opportunity to participate, "
            "contribute, and succeed."
        )
        return context


class AboutView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["content"] = content_map()
        context["values"] = [
            ("Inclusivity", "Creating spaces, systems, and opportunities that promote equal participation and leave no one behind."),
            ("Integrity", "Upholding honesty, transparency, ethical conduct, and responsible stewardship in all engagements."),
            ("Empowerment", "Equipping people with the knowledge, skills, confidence, and opportunities to shape their own futures."),
            ("Social Justice", "Challenging systemic inequalities, exclusion, discrimination, and harmful social norms."),
            ("Collaboration", "Working with communities, governments, civil society, development partners, academia, media, and the private sector."),
            ("Accountability", "Committing to measurable impact, responsible use of resources, continuous learning, and transparent reporting."),
            ("Respect", "Valuing the dignity, perspectives, experiences, and contributions of every individual and community."),
        ]
        return context


class AreasOfFocusView(TemplateView):
    template_name = "pages/areas_of_focus.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["content"] = content_map()
        context["areas"] = AreaOfFocus.objects.filter(is_published=True)
        context["pillars"] = FOCUS_PILLARS
        context["strategic_objectives"] = STRATEGIC_OBJECTIVES
        context["approaches"] = APPROACHES
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


class NewsView(TemplateView):
    template_name = "pages/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news_items"] = NEWS_ITEMS
        return context
