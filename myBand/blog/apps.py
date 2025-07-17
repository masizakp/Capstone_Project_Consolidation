"""
    Configuration for the blog application.

    Sets the default primary key field type for models to BigAutoField.
    Specifies the app name as 'blog'.
    """
from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"
