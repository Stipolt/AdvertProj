from django.contrib import admin
from .models import Advertise, Category, Reply, AdCat

# Register your models here.
admin.site.register(Advertise)
admin.site.register(Category)
admin.site.register(Reply)
admin.site.register(AdCat)