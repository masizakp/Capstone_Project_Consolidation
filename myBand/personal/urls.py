"""
    URL configuration for the Django project.

    This module maps URL paths to corresponding view functions.
    Currently, it routes:
    - the root URL ('') to the home_screen_view in the personal app
    - the 'admin/' URL to the Django admin site
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from personal import views


# Define URL patterns to map paths to views
urlpatterns = [
    # Route for the Django admin interface
    # path("admin/", admin.site.urls),

    # Route for the home page and eshopping page
    path("", views.home_screen_view, name="home"),
    path("eshopping/", views.eshopping_view, name="eshopping"),
    path("extrapage/", views.meetsetshehla_view, name="extrapage"),
    path("order/", views.order_view, name="order"),
    path("success/", views.success_view, name="success"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
