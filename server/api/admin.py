from django.contrib import admin
from .models import *

@admin.register(Сategory)
class CategoryAdmin(admin.ModelAdmin):
    pass
