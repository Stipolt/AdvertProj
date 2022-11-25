from django.apps import AppConfig
from django.core.signals import request_finished


class AdappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AdApp'

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals
        # Explicitly connect a signal handler.
        request_finished.connect(signals.reply_to_reply)