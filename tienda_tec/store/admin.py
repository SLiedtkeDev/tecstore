from django.contrib import admin

from .models import Product


class Product_Admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'description', 'updated')


admin.site.register(Product, Product_Admin)
