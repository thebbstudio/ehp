from django.contrib import admin
from .models import *

# Добавление в админ панель возможности редактирования категории
@admin.register(Сategory)
class CategoryAdmin(admin.ModelAdmin):
    pass
