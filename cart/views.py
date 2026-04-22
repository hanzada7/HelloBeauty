from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view

from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer, CartItemCreateSerializer


@extend_schema_view(
    list=extend_schema(summary='Получить корзину', tags=['Cart']),
    add_item=extend_schema(summary='Добавить товар', tags=['Cart']),
    update_item=extend_schema(summary='Изменить количество', tags=['Cart']),
    remove_item=extend_schema(summary='Удалить товар', tags=['Cart']),
    clear=extend_schema(summary='Очистить корзину', tags=['Cart']),
)
class CartViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def _get_or_create_cart(self, user):
        cart, _ = Cart.objects.get_or_create(user=user)
        return cart

    def list(self, request):
        
        cart = self._get_or_create_cart(request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='add')
    def add_item(self, request):
        
        cart = self._get_or_create_cart(request.user)
        serializer = CartItemCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product_id = serializer.validated_data['product_id']
        quantity = serializer.validated_data['quantity']

        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product_id=product_id,
            defaults=serializer.validated_data,
        )

        if not created:
            item.quantity += quantity
            item.save()

        return Response(
            CartSerializer(cart).data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )

    @action(detail=True, methods=['patch'], url_path='update')
    def update_item(self, request, pk=None):
        """Изменить количество товара в корзине."""
        cart = self._get_or_create_cart(request.user)

        try:
            item = cart.items.get(pk=pk)
        except CartItem.DoesNotExist:
            return Response(
                {'error': 'Товар не найден в корзине.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        quantity = request.data.get('quantity')
        if not quantity or int(quantity) < 1:
            return Response(
                {'error': 'Укажите количество не менее 1.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        item.quantity = int(quantity)
        item.save()

        return Response(CartSerializer(cart).data)

    @action(detail=True, methods=['delete'], url_path='remove')
    def remove_item(self, request, pk=None):
        
        cart = self._get_or_create_cart(request.user)

        try:
            item = cart.items.get(pk=pk)
        except CartItem.DoesNotExist:
            return Response(
                {'error': 'Товар не найден в корзине.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        item.delete()
        return Response(CartSerializer(cart).data)

    @action(detail=False, methods=['delete'], url_path='clear')
    def clear(self, request):
        
        cart = self._get_or_create_cart(request.user)
        cart.items.all().delete()
        return Response(CartSerializer(cart).data)
