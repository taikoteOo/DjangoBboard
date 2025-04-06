from django import forms
from django.contrib.auth.models import User
from .models import Ad


class AdForm(forms.Form):
    title = forms.CharField(max_length=200, label='Заголовок')
    type = forms.CharField(max_length=50, label='Категория')
    text = forms.CharField(widget=forms.Textarea, label='Текст поста')
    author = forms.ModelChoiceField(queryset=User.objects.all(), label='Автор')
    price = forms.CharField(max_length=20, label='Цена')