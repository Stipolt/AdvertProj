from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.models import User
from AdApp.models import Advertise, Reply

from .models import Profile
import pyotp

from django.contrib.auth import authenticate, login


def send_otp(email, otp):
    send_mail(
        'Confirm your registration',
        f'Your confirmation code is {otp}',
        'egorkabox@yandex.ru',
        [email],
        fail_silently=False,
    )
    return None


def login_attempt(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        profile = Profile.objects.filter(email=email).first()
        user = User.objects.filter(email=email).first()

        if profile is None:
            context = {'message': 'User not found', 'class': 'danger'}
            return render(request, 'login.html', context)

        if user.check_password(password):
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
        else:
            context = {'message': 'Incorrect password', 'class': 'danger'}
            return render(request, 'login.html', context)

        return redirect('/')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        check_user = User.objects.filter(email=email).first()
        check_profile = Profile.objects.filter(email=email).first()

        if check_user or check_profile:
            context = {'message': 'User already exists', 'class': 'danger'}
            return render(request, 'register.html', context)

        user = User.objects.create_user(email=email, username=username, password=password)
        user.set_password(password)
        user.is_active = False
        user.save()
        totp = pyotp.TOTP('base32secret3232')
        otp = totp.now()
        profile = Profile(user=user, email=email, otp=otp)
        profile.save()
        send_otp(email, otp)
        request.session['email'] = email
        return redirect('otp')
    return render(request, 'register.html')


def otp(request):
    email = request.session['email']
    context = {'email': email}
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = Profile.objects.filter(email=email).first()

        if otp == profile.otp:
            user = User.objects.filter(email=email).first()
            user.is_active = True
            user.save()
            user = authenticate(username=user.username, password=user.password)
            return redirect('/')
        else:
            print('Wrong')

            context = {'message': 'Wrong OTP', 'class': 'danger', 'email': email}
            return render(request, 'otp.html', context)

    return render(request, 'otp.html', context)


class LogView(LoginView):
    template_name = 'login.html'


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    try:
        advertise = Advertise.objects.filter(user=user)
    except ObjectDoesNotExist:
        advertise = None
    try:
        reply = Reply.objects.filter(advertise__in=advertise)[:]
    except ObjectDoesNotExist:
        reply = None

    # advertise = get_object_or_404(Advertise, user=user)
    return render(request, 'profile.html', {'profile': profile,
                                            'user': user,
                                            'advertise': advertise,
                                            'reply': reply,
                                            })
