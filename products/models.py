from django.db import models


class Category(models.Model):
    """
    Категория товаров.
    Например: Уход за лицом, Уход за волосами, Парфюм и т.д.
    """
    name = models.CharField(
        max_length=200,
        verbose_name='Название категории',
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='URL-адрес',
        help_text='Автоматически заполняется из названия',
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание',
    )
    image = models.ImageField(
        upload_to='categories/',
        blank=True,
        null=True,
        verbose_name='Изображение категории',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Товар в магазине.
    """
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products',
        verbose_name='Категория',
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Название товара',
    )
    brand = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Бренд',
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание',
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена (сом)',
    )
    old_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Старая цена (для скидки)',
    )
    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True,
        verbose_name='Главное изображение',
    )
    stock = models.PositiveIntegerField(
        default=0,
        verbose_name='Остаток на складе',
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name='Доступен для покупки',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Последнее обновление',
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    @property
    def discount_percent(self):
        """Считаем процент скидки если есть старая цена."""
        if self.old_price and self.old_price > self.price:
            discount = (self.old_price - self.price) / self.old_price * 100
            return round(discount)
        return 0

    @property
    def in_stock(self):
        return self.stock > 0
