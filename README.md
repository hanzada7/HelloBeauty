# HelloBeauty — API для интернет-магазина косметики

Первый интернет-магазин уходовой косметики в Кыргызстане 🇰🇬

## Технологии
- Python 3.11
- Django 4.2
- Django REST Framework
- JWT аутентификация
- Docker + docker-compose
- SQLite (разработка)

## Как запустить через Docker (рекомендуется)

```bash
# 1. Склонируй репозиторий
git clone https://github.com/hanzada7/HelloBeauty.git
cd HelloBeauty

# 2. Создай .env файл
cp .env.example .env

# 3. Запусти через Docker
docker-compose up --build

# Сайт будет на http://localhost:8000
# Документация API: http://localhost:8000/api/docs/
```

## Как запустить локально (без Docker)

```bash
# 1. Создай виртуальное окружение
python -m venv venv
source venv/bin/activate   # Linux/Mac
# venv\Scripts\activate   # Windows

# 2. Установи зависимости
pip install -r requirements.txt

# 3. Создай .env
cp .env.example .env

# 4. Применить миграции
python manage.py migrate

# 5. Создать суперпользователя (для входа в /admin/)
python manage.py createsuperuser

# 6. Запустить сервер
python manage.py runserver
```

## API Endpoints

### Аутентификация (`/api/accounts/`)
| Метод | URL | Описание |
|-------|-----|----------|
| POST | `/api/accounts/register/` | Регистрация |
| POST | `/api/accounts/login/` | Войти (получить токен) |
| POST | `/api/accounts/logout/` | Выйти |
| POST | `/api/accounts/token/refresh/` | Обновить токен |
| GET/PUT | `/api/accounts/profile/` | Мой профиль |
| PUT | `/api/accounts/change-password/` | Сменить пароль |

### Товары (`/api/products/`)
| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/products/` | Список всех товаров |
| GET | `/api/products/?search=крем` | Поиск товаров |
| GET | `/api/products/?category=1` | Товары категории |
| GET | `/api/products/?ordering=price` | Сортировка по цене |
| GET | `/api/products/<id>/` | Детальная страница товара |
| GET | `/api/products/featured/` | Товары со скидкой |
| GET | `/api/products/categories/` | Все категории |
| GET | `/api/products/categories/<id>/` | Одна категория |
| GET | `/api/products/category/<id>/` | Товары по категории |

### Корзина (`/api/cart/`) — нужна авторизация!
| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/cart/` | Моя корзина |
| POST | `/api/cart/add/` | Добавить товар |
| PATCH | `/api/cart/<id>/update/` | Изменить количество |
| DELETE | `/api/cart/<id>/remove/` | Удалить товар |
| DELETE | `/api/cart/clear/` | Очистить корзину |

## Структура проекта

```
HelloBeauty/
├── accounts/       # Пользователи и аутентификация
├── cart/           # Корзина покупателя
├── products/       # Товары и категории (новый!)
├── users/          # Зарезервировано для будущего
├── HelloBeauty/    # Настройки проекта
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Что можно добавить в будущем
- [ ] Заказы (Orders)
- [ ] Избранное (Wishlist)
- [ ] Отзывы на товары (Reviews)
- [ ] Несколько изображений у товара
- [ ] PostgreSQL вместо SQLite
- [ ] Фронтенд на React/Vue
