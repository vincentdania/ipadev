from django.core.management.base import BaseCommand

from apps.core.models import SiteSetting
from apps.pages.models import AreaOfFocus, ContentListItem, GalleryImage, PageContent
from apps.people.models import TeamMember


class Command(BaseCommand):
    help = "Seed initial IPADEV content for local development or first deployment."

    def handle(self, *args, **options):
        site_settings = {
            "head_office_address": "Flat 2B1E Admiralty Estate\nAsokoro, Abuja, Nigeria",
            "phone": "+234 706 406 2121",
            "primary_email": "info@ipadev.ng",
            "alternative_email": "margaret.fagboyo@ipadev.ng",
        }
        for name, value in site_settings.items():
            SiteSetting.objects.update_or_create(name=name, defaults={"value": value})

        PageContent.objects.update_or_create(
            key="hero",
            defaults={
                "title": "Building Inclusive Pathways for Sustainable Development, Social Justice, and Equal Opportunity",
                "body": (
                    "IPADEV is a Nigerian non-profit organization established to advance inclusive "
                    "development, social justice, gender equality, and equitable access to opportunities "
                    "for vulnerable and underserved populations."
                ),
            },
        )
        PageContent.objects.update_or_create(
            key="mission_vision",
            defaults={
                "title": "Our Mission & Vision",
                "body": (
                    "Our mission is to promote equal opportunities, social justice, and community empowerment "
                    "through inclusive policies, capacity building, and advocacy for societal transformation.\n\n"
                    "Our vision is a just and inclusive society where every individual, regardless of gender, "
                    "background, or status, has equal opportunities to thrive and contribute to sustainable development."
                ),
            },
        )
        page_blocks = [
            (
                "home_mission",
                "Equal opportunity, social justice, and community empowerment",
                (
                    "IPADEV was founded from a deep recognition that many individuals and communities "
                    "remain excluded from the benefits of development, not because they lack potential, "
                    "but because the systems around them were not intentionally designed to include them.\n\n"
                    "Our mission is to promote equal opportunities, social justice, and community "
                    "empowerment through inclusive policies, capacity building, and advocacy for societal "
                    "transformation."
                ),
            ),
            (
                "home_focus",
                "Five pathways for inclusive transformation",
                (
                    "IPADEV's work is driven by the understanding that sustainable development requires "
                    "inclusive systems, empowered communities, responsive institutions, and equitable "
                    "access to opportunities."
                ),
            ),
            (
                "home_why",
                "Turning inclusion gaps into practical pathways",
                (
                    "Many people remain unheard, underrepresented, or excluded from governance, economic "
                    "participation, leadership opportunities, and social protection systems. IPADEV exists "
                    "to strengthen the connection between citizens, institutions, and development processes."
                ),
            ),
            (
                "about_intro",
                "Building inclusive pathways for equal opportunity.",
                (
                    "IPADEV is a Nigerian non-profit organization established to advance inclusive "
                    "development, social justice, gender equality, and equitable access to opportunities "
                    "for vulnerable and underserved populations."
                ),
            ),
            (
                "about_story",
                "Our story: practical pathways for inclusion",
                (
                    "IPADEV was founded from a deep recognition that many individuals and communities "
                    "remain excluded from the benefits of development, not because they lack potential, "
                    "but because the systems around them were not intentionally designed to include them.\n\n"
                    "The organization works to create practical and sustainable pathways for inclusion by "
                    "strengthening community voices, supporting citizen participation, promoting accountable "
                    "governance, expanding opportunities for women and marginalized groups, and building "
                    "institutional and community capacity for long-term social change.\n\n"
                    "IPADEV believes development becomes meaningful only when it is inclusive, participatory, "
                    "and rooted in the lived realities of the people it seeks to serve."
                ),
            ),
            (
                "contact_intro",
                "Start a strategic conversation",
                (
                    "Have questions, feedback, or a partnership idea? Reach out and our team will get back "
                    "to you as soon as possible."
                ),
            ),
        ]
        for key, title, body in page_blocks:
            PageContent.objects.update_or_create(
                key=key,
                defaults={"title": title, "body": body, "is_published": True},
            )
        PageContent.objects.update_or_create(
            key="areas_background",
            defaults={
                "title": "Background",
                "body": (
                    "IPADEV's work is driven by the understanding that sustainable development requires "
                    "inclusive systems, empowered communities, responsive institutions, and equitable access "
                    "to opportunities.\n\n"
                    "The organization adopts an integrated approach that combines advocacy, community "
                    "engagement, institutional strengthening, policy influence, leadership development, and "
                    "strategic partnerships to address systemic barriers that limit participation and human "
                    "development.\n\n"
                    "Our strategic focus areas reflect both the realities faced by vulnerable populations "
                    "and the pathways required to build more inclusive and resilient communities."
                ),
            },
        )

        areas = [
            ("Gender Equality and Women's Empowerment", "Advancing the rights, participation, leadership, and socio-economic empowerment of women and girls."),
            ("Inclusive Governance and Active Citizenship", "Promoting governance systems that are inclusive, participatory, transparent, and accountable to citizens."),
            ("Social Justice and Inclusion", "Promoting dignity, fairness, and respect for people facing social, economic, gender, or physical exclusion."),
            ("Capacity Building and Institutional Strengthening", "Supporting organizations, institutions, community structures, networks, and emerging leaders to strengthen effectiveness and resilience."),
            ("Sustainable Development and Community Resilience", "Promoting locally driven approaches that improve livelihoods, strengthen resilience, and support long-term transformation."),
        ]
        for index, (title, description) in enumerate(areas, start=1):
            AreaOfFocus.objects.update_or_create(
                title=title,
                defaults={"description": description, "sort_order": index, "is_published": True},
            )

        list_items = {
            "about_values": [
                ("Inclusivity", "Creating spaces, systems, and opportunities that promote equal participation and leave no one behind.", "verified_user", ""),
                ("Integrity", "Upholding honesty, transparency, ethical conduct, and responsible stewardship in all engagements.", "gpp_good", ""),
                ("Empowerment", "Equipping people with the knowledge, skills, confidence, and opportunities to shape their own futures.", "diversity_1", ""),
                ("Social Justice", "Challenging systemic inequalities, exclusion, discrimination, and harmful social norms.", "balance", ""),
                ("Collaboration", "Working with communities, governments, civil society, development partners, academia, media, and the private sector.", "handshake", ""),
                ("Accountability", "Committing to measurable impact, responsible use of resources, continuous learning, and transparent reporting.", "fact_check", ""),
                ("Respect", "Valuing the dignity, perspectives, experiences, and contributions of every individual and community.", "volunteer_activism", ""),
            ],
            "strategic_objectives": [
                ("Promote inclusion and equitable access to opportunities.", "", "check_circle", ""),
                ("Strengthen institutions and community systems.", "", "check_circle", ""),
                ("Advance gender equality and social justice.", "", "check_circle", ""),
                ("Support leadership and capacity development.", "", "check_circle", ""),
                ("Encourage citizen participation and accountability.", "", "check_circle", ""),
                ("Foster innovation and sustainable development solutions.", "", "check_circle", ""),
                ("Deliver measurable and lasting impact within communities.", "", "check_circle", ""),
            ],
            "approaches": [
                ("Policy advocacy and systems engagement", "", "", ""),
                ("Community mobilization and citizen engagement", "", "", ""),
                ("Capacity strengthening and leadership development", "", "", ""),
                ("Strategic partnerships and collaboration", "", "", ""),
                ("Research, learning, and evidence generation", "", "", ""),
                ("Inclusive programme design and implementation", "", "", ""),
                ("Accountability and sustainable impact", "", "", ""),
            ],
            "resource_items": [
                (
                    "Women's leadership and political participation",
                    "IPADEV supports leadership development, mentorship, and gender-responsive systems that strengthen women's voices in decision-making spaces.",
                    "female",
                    "Focus Area · Gender Equality",
                ),
                (
                    "Civic education and citizen engagement",
                    "The organization promotes public dialogue, stakeholder engagement, citizen feedback mechanisms, and democratic participation.",
                    "campaign",
                    "Focus Area · Active Citizenship",
                ),
                (
                    "Capacity building and organizational resilience",
                    "IPADEV provides practical support for leadership systems, programme effectiveness, accountability, and long-term sustainability.",
                    "hub",
                    "Focus Area · Institutional Strengthening",
                ),
            ],
        }
        for section, items in list_items.items():
            for index, (title, body, icon, eyebrow) in enumerate(items, start=1):
                ContentListItem.objects.update_or_create(
                    section=section,
                    title=title,
                    defaults={
                        "body": body,
                        "icon_name": icon,
                        "eyebrow": eyebrow,
                        "sort_order": index,
                        "is_published": True,
                    },
                )

        gallery_images = [
            (
                "Dr. Margaret Fagboyo with a community beneficiary",
                "Community engagement",
                "img/ipadev-gallery/dr-fagboyo-beneficiary.jpeg",
            ),
            (
                "Guests at the official launch of IPADEV",
                "Official launch",
                "img/ipadev-gallery/ipadev-launch-presentation.jpeg",
            ),
            (
                "IPADEV official launch media briefing banner",
                "Media briefing",
                "img/ipadev-gallery/official-launch-media-briefing.jpeg",
            ),
            (
                "Group photograph from the IPADEV launch",
                "Launch participants",
                "img/ipadev-gallery/ipadev-launch-group.jpeg",
            ),
        ]
        for index, (title, caption, static_path) in enumerate(gallery_images, start=1):
            GalleryImage.objects.update_or_create(
                title=title,
                defaults={
                    "caption": caption,
                    "alt_text": title,
                    "static_path": static_path,
                    "sort_order": index,
                    "is_published": True,
                },
            )

        TeamMember.objects.update_or_create(
            name="Dr. Margaret Fagboyo",
            defaults={
                "role": "Executive Director",
                "bio": (
                    "Dr. Margaret Fagboyo is a respected development practitioner, governance advocate, "
                    "and social inclusion expert with decades of experience spanning international "
                    "development, public sector governance, policy engagement, institutional strengthening, "
                    "and civic leadership."
                ),
                "is_executive_director": True,
                "photo_static_path": "img/margaret-fagboyo.jpg",
                "vision": "A just and inclusive society where every individual, regardless of gender, background, or status, has equal opportunities to thrive and contribute to sustainable development.",
                "message": (
                    "Under her leadership, IPADEV is being positioned as a values-driven organization "
                    "committed to ethical leadership, inclusive development, institutional accountability, "
                    "strategic partnerships, and measurable social impact."
                ),
                "sort_order": 1,
                "is_active": True,
            },
        )
        board_members = [
            ("Adesina Fagbenro-Byron", "Board Member", "Experienced board member with expertise in governance and strategic planning.", "img/dr-adesina.jpeg"),
            ("Abiodun Essiet", "Board Member", "Dedicated board member focused on organizational development and community engagement.", "img/essiet.jpeg"),
            ("Olamide Juliana Falana", "Board Member", "Strategic board member with background in policy development and implementation.", "img/olamide-falana.jpeg"),
            ("Olubunmi Adelugba", "Board Member", "Experienced board member committed to advancing organizational mission and values.", "img/adelugba.jpeg"),
            ("Dominion Dolapo Fagboyo", "Board Member", "Dedicated board member with expertise in financial oversight and strategic planning.", "img/dominion.jpeg"),
            ("Samuel Ruth Chadi", "Secretary", "Board secretary with strong organizational skills and attention to detail.", "img/ruth.jpeg"),
        ]
        for index, (name, role, bio, image) in enumerate(board_members, start=10):
            TeamMember.objects.update_or_create(
                name=name,
                defaults={
                    "role": role,
                    "bio": bio,
                    "photo_static_path": image,
                    "is_executive_director": False,
                    "sort_order": index,
                    "is_active": True,
                },
            )

        self.stdout.write(self.style.SUCCESS("Seeded IPADEV starter content."))
