from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'price')


admin.site.register(Product, ProductAdmin)
