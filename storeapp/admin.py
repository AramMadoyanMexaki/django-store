from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "rest_weight", "buy_weight", "add_weight", "created_at", "updated_at", "photo", "category", "price")
    search_fields = ("name",)


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoriesAdmin)