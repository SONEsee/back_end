from django.apps import AppConfig


class UtilityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'utility'


from django.apps import AppConfig

class UtilityAppConfig(AppConfig):  
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'utility_app'  

    def ready(self):
        import utility.signals  