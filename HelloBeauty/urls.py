from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # Админка Django
    path('admin/', admin.site.urls),

    # Аккаунты (регистрация, логин, профиль)
    path('api/accounts/', include('accounts.urls')),

    # Users (пока пустой)
    path('api/users/', include('users.urls')),

    # Корзина
    path('api/cart/', include('cart.urls')),

    # Товары и категории - новый раздел!
    path('api/products/', include('products.urls')),

    # Swagger документация
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

# Это нужно чтобы картинки товаров отдавались в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
