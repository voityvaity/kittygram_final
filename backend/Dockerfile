# kittygram_backend/Dockerfile
# Создать образ на основе базового слоя,
# который содержит файлы ОС и интерпретатор Python 3.12.
FROM python:3.12

# Добавляем установку системных зависимостей
RUN apt-get update && apt-get install -y \
    postgresql-client \
    libpq-dev \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libopenjp2-7-dev \
    libtiff5-dev \
    libwebp-dev \
    && rm -rf /var/lib/apt/lists/*

# Переходим в образе в директорию /app: в ней будем хранить код проекта.
# Если директории с указанным именем нет, она будет создана. 
# Название директории может быть любым.
WORKDIR /app
# Дальнейшие инструкции будут выполняться в директории /app

# Обновляем pip до последней версии
RUN pip install --upgrade pip

RUN pip install gunicorn==23.0.0

# Скопировать с локального компьютера файл зависимостей
# в текущую директорию (текущая директория — это /app).
COPY requirements.txt .

# Выполнить в текущей директории команду терминала
# для установки зависимостей.
RUN pip install -r requirements.txt --no-cache-dir

# Скопировать всё необходимое содержимое 
# той директории локального компьютера, где сохранён Dockerfile,
# в текущую рабочую директорию образа — /app.
COPY . .

# При старте контейнера запустить сервер разработки.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "kittygram_backend.wsgi"]