from django.contrib.auth.mixins import LoginRequiredMixin
from django.dispatch import receiver
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filter import AdFilter
from .forms import AdForm, ReplyForm
from .models import *


# @receiver
# def email_reply_to_reply(sender, instance, created, **kwargs):
#     subject = f'{instance.client_name} {instance.date.strftime("%d %m %Y")}'
#     mail_managers(
#         subject=subject,
#         message=instance.message,
#     )
#
#     post_save.connect(notify_managers_appointment, sender=Appointment)


def email_reply(pk):
    ad = Advertise.objects.get(id=pk)
    email = ad.user.email
    send_mail(
        'You have a reply to your ad! Check in!',
        f'Hello u get a reply for your ad',
        'egorkabox@yandex.ru',
        [email],
        fail_silently=False,
    )


class AdvertList(ListView):
    model = Advertise
    ordering = 'time_pub'
    template_name = 'advertise.html'
    context_object_name = 'ads'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AdFilter(self.request.GET, queryset)
        return self.filterset.qs


class AdvertDetail(DetailView):
    model = Advertise
    template_name = 'ad_detail.html'
    context_object_name = 'ad'


class AdvertCreate(LoginRequiredMixin, CreateView):
    form_class = AdForm
    model = Advertise
    template_name = 'ad_edit.html'


class AdvertEdit(LoginRequiredMixin, UpdateView):
    form_class = AdForm
    model = Advertise
    template_name = 'ad_edit.html'


class SendReply(LoginRequiredMixin, View):
    def post(self, request, pk):
        form = ReplyForm(request.POST)
        advertise = Advertise.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.advertise = advertise
            form.save()
            email_reply(pk)
        return redirect(advertise.get_absolute_url())


class ReplyDeleteView(LoginRequiredMixin, DeleteView):
    model = Reply
    template_name = 'delete_reply.html'
    success_url = reverse_lazy('ads')
