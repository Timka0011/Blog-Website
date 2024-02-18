from django.urls import path
from .views import (
    index,
    about_us,
    Blog,
    DetailBlog,
    CreateNewsView,
    CreateTeamView,
    ContactView,
    CreateContactView,
)

urlpatterns = [
    path("", index, name="home"),
    path("about/", about_us, name="about_us"),
    path("new/", CreateNewsView.as_view(), name="create_news"),
    path("blog/<int:pk>/", DetailBlog.as_view(), name="blog_detail"),
    path("blog/", Blog.as_view(), name="blog"),
    path("teamnew/", CreateTeamView.as_view(), name="teamnew"),
    path("contact/", ContactView.as_view(), name="contact"),
    # path("contact/", CreateContactView.as_view(), name="contact"),
]
