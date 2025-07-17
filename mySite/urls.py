"""
URL configuration for the Django project.

This file defines the mapping between URL paths and the views that handle them.
Each path in the urlpatterns list routes a URL to a view function.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# List of URL patterns to route incoming HTTP requests
urlpatterns = [
    # Admin site URL
    path("admin/", admin.site.urls),

    # Home page view (root URL)
    path("", include('personal.urls')),

    path('blog/', include('blog.urls')),

    path('polls/',include('polls.urls')),

    path('user_auth/', include('user_auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
