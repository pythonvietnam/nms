from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    name = 'apps.base'
    verbose_name = "User's Profile"

    def ready(self):
        from apps.base import signals