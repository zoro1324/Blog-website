from django.apps import AppConfig
from django.db.models.signals import post_migrate



class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    def ready(self):
        from .signals import Create_Group
        post_migrate.connect(Create_Group)
