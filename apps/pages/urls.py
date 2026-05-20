from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("areas-of-focus/", views.AreasOfFocusView.as_view(), name="areas_of_focus"),
    path("get-involved/", views.GetInvolvedView.as_view(), name="get_involved"),
    path("impact/", views.ImpactView.as_view(), name="impact"),
    path("news/", views.NewsView.as_view(), name="news"),
    path("blog/", views.BlogListView.as_view(), name="blog_list"),
    path("blog/<slug:slug>/", views.BlogDetailView.as_view(), name="blog_detail"),
]
