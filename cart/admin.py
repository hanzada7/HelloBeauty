from django.contrib import admin
from django.contrib import admin
from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ('total_price', 'added_at')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_items', 'total_price', 'created_at', 'updated_at')
    readonly_fields = ('total_price', 'total_items', 'created_at', 'updated_at')
    inlines = [CartItemInline]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'cart', 'price', 'quantity', 'total_price', 'added_at')
    list_filter = ('cart__user',)
    search_fields = ('product_name',)
    readonly_fields = ('total_price', 'added_at')
