from django.urls import path
from .views import (
    CategoryListView,
    CategoryDetailView,
    ProductListView,
    ProductDetailView,
    ProductsByCategoryView,
    FeaturedProductsView,
)

urlpatterns = [
    # Категории
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    # Товары
    path('', ProductListView.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('category/<int:category_id>/', ProductsByCategoryView.as_view(), name='products-by-category'),
    path('featured/', FeaturedProductsView.as_view(), name='featured-products'),
]
