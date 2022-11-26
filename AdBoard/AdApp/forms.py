from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Advertise, Reply


class AdForm(forms.ModelForm):
    content = forms.CharField(min_length=10)

    class Meta:
        model = Advertise
        fields = ['header',
                  'content',
                  'category',
                  'photo',
                  'file',
                  ]

        def clean(self):
            cleaned_data = super().clean()
            content = cleaned_data.get("content")
            header = cleaned_data.get('header')


            if header == content:
                raise ValidationError(
                    "Заголовок не может быть идентичен названию"
                )

            return cleaned_data


class ReplyForm(forms.ModelForm):

     class Meta:
        model = Reply
        fields = ("name", "msg")
