from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Отображение категорий в Django Admin."""
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}  # slug заполняется автоматически из name
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Отображение товаров в Django Admin."""
    list_display = ['name', 'brand', 'category', 'price', 'stock', 'is_available', 'created_at']
    list_filter = ['is_available', 'category', 'brand']
    search_fields = ['name', 'brand', 'description']
    list_editable = ['price', 'stock', 'is_available']  # можно редактировать прямо в списке
    readonly_fields = ['created_at', 'updated_at']
