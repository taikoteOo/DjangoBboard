from django.contrib import admin
from .models import Ad, Category, GeneralCategory

admin.site.register(Ad)
admin.site.register(GeneralCategory)
admin.site.register(Category)
