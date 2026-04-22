from rest_framework import serializers
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = CartItem
        fields = (
            'id',
            'product_id',
            'product_name',
            'price',
            'quantity',
            'image',
            'total_price',
            'added_at',
        )
        read_only_fields = ('id', 'added_at', 'total_price')


class CartItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('product_id', 'product_name', 'price', 'quantity', 'image')

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError('Количество должно быть не менее 1.')
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Цена должна быть больше 0.')
        return value


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.ReadOnlyField()
    total_items = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = ('id', 'items', 'total_price', 'total_items', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')