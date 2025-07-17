"""
    URL configuration for the blog app.

    Defines URL patterns that display:
    - A list of the 25 most recent blog posts (ordered by date descending) at the root URL.
    - Detailed view of a single blog post identified by its primary key (pk).

    Uses Django's generic class-based views ListView and DetailView.
    """
from django.views.generic import ListView, DetailView
from django.urls import path
from blog.models import Post

urlpatterns = [
    path('',
        ListView.as_view(
            queryset=Post.objects.all().order_by("-date")[:25],
            template_name="blog.html"
        )
    ),
    path('<int:pk>/',
        DetailView.as_view(
            model=Post,
            template_name="post.html"
        )
    ),
]
