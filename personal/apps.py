"""
    Configuration for the personal application.

    Sets the default primary key field type for models to BigAutoField.
    Specifies the app name as 'personal'.
    """
from django.apps import AppConfig


class PersonalConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "personal"
