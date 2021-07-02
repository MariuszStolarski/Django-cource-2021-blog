from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),  # for landing page
    path("posts", views.posts, name="posts-page"),  # for the post app
    # for the specific post, via slug / a dynamic url
    path("posts/<slug:a_slug_variable>",
         views.post_details, name="post-details-page")
]
