from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.engagement.api import ContactSubmissionViewSet, NewsletterSubscriberViewSet
from apps.pages.api import AreaOfFocusViewSet, PageContentViewSet
from apps.people.api import TeamMemberViewSet

admin.site.site_header = "IPADEV Admin"
admin.site.site_title = "IPADEV Admin"
admin.site.index_title = "Website content management"

router = DefaultRouter()
router.register("content", PageContentViewSet)
router.register("areas-of-focus", AreaOfFocusViewSet)
router.register("team", TeamMemberViewSet)
router.register("contact-submissions", ContactSubmissionViewSet)
router.register("newsletter-subscribers", NewsletterSubscriberViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("api/", include(router.urls)),
    path("", include("apps.pages.urls")),
    path("", include("apps.people.urls")),
    path("", include("apps.engagement.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
