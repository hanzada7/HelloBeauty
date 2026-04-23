from rest_framework import generics, filters, status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, Product
from .serializers import (
    CategorySerializer,
    ProductListSerializer,
    ProductDetailSerializer,
)


# =====================
# КАТЕГОРИИ
# =====================

class CategoryListView(generics.ListAPIView):
    """
    GET /api/products/categories/
    Список всех категорий - доступен всем без авторизации.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class CategoryDetailView(generics.RetrieveAPIView):
    """
    GET /api/products/categories/<id>/
    Одна категория с описанием.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


# =====================
# ТОВАРЫ
# =====================

class ProductListView(generics.ListAPIView):
    """
    GET /api/products/
    Список товаров с фильтрацией и поиском.

    Параметры:
    - search=крем          (поиск по названию и бренду)
    - category=1           (фильтр по категории)
    - is_available=true    (только доступные)
    - ordering=price       (сортировка: price, -price, name, -name)
    """
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]
    
    # Подключаем поиск и фильтры
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    
    # По каким полям искать через ?search=
    search_fields = ['name', 'brand', 'description']
    
    # По каким полям фильтровать через ?category=1
    filterset_fields = ['category', 'is_available']
    
    # По каким полям сортировать через ?ordering=price
    ordering_fields = ['price', 'name', 'created_at']
    ordering = ['-created_at']  # по умолчанию - новые первые

    def get_queryset(self):
        queryset = Product.objects.select_related('category').all()
        return queryset


class ProductDetailView(generics.RetrieveAPIView):
    """
    GET /api/products/<id>/
    Детальная страница товара.
    """
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductDetailSerializer
    permission_classes = [AllowAny]


class ProductsByCategoryView(generics.ListAPIView):
    """
    GET /api/products/category/<category_id>/
    Все товары определённой категории.
    """
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(
            category_id=category_id,
            is_available=True,
        ).select_related('category')


class FeaturedProductsView(generics.ListAPIView):
    """
    GET /api/products/featured/
    Товары со скидкой (у которых есть old_price).
    Можно использовать на главной странице сайта.
    """
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Product.objects.filter(
            is_available=True,
            old_price__isnull=False,  # только если есть старая цена
        ).select_related('category')[:12]  # берём первые 12
