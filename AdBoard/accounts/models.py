from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    otp = models.CharField(max_length=6)

    def __str__(self):
        return str(self.user.username)
