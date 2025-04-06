from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User


class Ad(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    type = models.CharField(max_length=50, verbose_name='Категория')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст объявления')
    price = models.CharField(max_length=20, verbose_name='Цена')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания', editable=False)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title