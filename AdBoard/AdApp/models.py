from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Advertise(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    header = models.CharField(max_length=255)
    content = models.TextField()
    time_pub = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, through='AdCat')
    file = models.FileField("Video", blank=True)
    photo = models.ImageField("Image", blank=True)


    def get_absolute_url(self):
        return reverse('ad_detail', args=[str(self.id)])


class Reply(models.Model):
    name = models.CharField("Имя", max_length=30)
    msg = models.TextField(max_length=200)
    advertise = models.ForeignKey(Advertise, verbose_name="Объявление", on_delete=models.CASCADE)


class AdCat(models.Model):
    ad = models.ForeignKey(Advertise, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)




