from django.contrib import admin
from.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']

@admin.register(Tovar)
class TovarAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'category' ,'text', 'price', 'count']
    search_fields = ['name', 'category__name']
    list_filter = ['name', 'price', 'count', 'category']