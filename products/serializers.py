from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий."""

    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'description',
            'image',
            'products_count',
            'created_at',
        )

    def get_products_count(self, obj):
        # Считаем сколько товаров в этой категории
        return obj.products.filter(is_available=True).count()


class ProductListSerializer(serializers.ModelSerializer):
    """
    Короткий сериализатор - для списка товаров.
    Не возвращаем лишние поля чтобы не грузить сеть.
    """
    category_name = serializers.CharField(source='category.name', read_only=True)
    discount_percent = serializers.ReadOnlyField()
    in_stock = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'brand',
            'category_name',
            'price',
            'old_price',
            'discount_percent',
            'image',
            'in_stock',
            'is_available',
        )


class ProductDetailSerializer(serializers.ModelSerializer):
    """
    Полный сериализатор - для страницы одного товара.
    Возвращаем все поля.
    """
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True,
        required=False,
        allow_null=True,
    )
    discount_percent = serializers.ReadOnlyField()
    in_stock = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'brand',
            'description',
            'category',
            'category_id',
            'price',
            'old_price',
            'discount_percent',
            'image',
            'stock',
            'in_stock',
            'is_available',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('id', 'created_at', 'updated_at')
