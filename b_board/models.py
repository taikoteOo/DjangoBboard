from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from slugify import slugify


class Ad(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    type = models.CharField(max_length=50, verbose_name='Категория')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст объявления')
    price = models.CharField(max_length=20, verbose_name='Цена')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания', editable=False)
    image = models.ImageField(upload_to='ads/', null=True, blank=True, verbose_name='Изображение')
    slug = models.SlugField(max_length=200, unique=True, editable=False, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:read_post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title
#
# class Category(models.Model):
#     general_category = models.CharField(max_length=50, verbose_name='Основная категория')
#     category_name = models.CharField(max_length=50, verbose_name='Подкатегория')
