from django.core.signals import request_finished
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail


# @receiver(request_finished)
# def email_reply_to_reply(request, sender, user, **kwargs):
#     send_mail(
#         'Ваш отклик принят',
#         f'Привет, ваш отклик принял {user.username}'
#         'egorkabox@yandex.ru',
#         [email],
#         fail_silently=False,
#     )
