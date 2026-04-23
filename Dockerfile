# Используем официальный Python образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Сначала копируем только requirements.txt
# (это кэшируется Docker'ом - если requirements не менялся, pip install пропускается)
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Теперь копируем весь проект
COPY . .

# Создаём папки для медиа и статики
RUN mkdir -p media staticfiles

# Открываем порт 8000
EXPOSE 8000

# Команда запуска:
# 1. Применяем миграции
# 2. Запускаем сервер
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
