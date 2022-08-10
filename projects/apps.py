from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projects'

    def ready(self):
        # Implicitly connect a signal handlers decorated with @receiver.
        from . import signals
        from uuid import uuid4
        # Explicitly connect a signal handler.
        signals.post_save.connect(signals.project_readiness, dispatch_uid=uuid4())
