from django.apps import AppConfig


class SuperadminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.superadmin'

    def ready(self):
        import apps.superadmin.signals
