from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail


@receiver(post_save)
def reply_to_reply(sender, **kwargs):
    return None