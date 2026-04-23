from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

# ВНИМАНИЕ: в продакшне SECRET_KEY нужно хранить в переменной окружения!
# Сейчас оставляем так для разработки
SECRET_KEY = 'django-insecure-*ud_6vnr5zk(e*=k(_1_at80cbqi$d(9#*#4b5^^3ngyj+7g7j'

DEBUG = True

ALLOWED_HOSTS = ['*']  # в продакшне сюда пишем наш домен: ['hellobeauty.kg']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Сторонние библиотеки
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_spectacular',
    'corsheaders',      # нужно для фронтенда
    'django_filters',   # фильтрация товаров
    
    # Наши приложения
    'accounts',
    'users',
    'cart',
    'products',  # новый app!
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # CORS - должен быть выше CommonMiddleware!
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'HelloBeauty.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'HelloBeauty.wsgi.application'

# База данных - sqlite3 для разработки
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'ru-ru'  # меняем на русский
TIME_ZONE = 'Asia/Bishkek'  # часовой пояс Бишкека!
USE_I18N = True
USE_TZ = True

# Статические файлы (CSS, JS)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Медиа файлы (картинки товаров и категорий)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Используем нашу кастомную модель User из accounts
AUTH_USER_MODEL = 'accounts.User'

# Настройки Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
}

# Настройки JWT токенов
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

# Swagger документация
SPECTACULAR_SETTINGS = {
    'TITLE': 'HelloBeauty API',
    'DESCRIPTION': 'API для интернет-магазина косметики HelloBeauty (Бишкек)',
    'VERSION': '1.0.0',
}

# CORS - разрешаем фронтенду обращаться к нашему API
# В разработке разрешаем все, в продакшне укажем конкретный домен
CORS_ALLOW_ALL_ORIGINS = True  # TODO: в продакшне поменять на CORS_ALLOWED_ORIGINS
