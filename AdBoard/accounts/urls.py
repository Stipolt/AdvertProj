from .views import *
from django.urls import path, include
from django.contrib.auth import views

urlpatterns = [

    path('login/', LogView.as_view(), name="login"),
    path('register/', register, name="register"),
    path('otp/', otp, name="otp"),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/<username>/', login_required(profile), name='profile'),
]
