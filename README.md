# Kittygram

Веб-приложение для публикации карточек котов и их достижений. Проект показывает полный путь backend-приложения: REST API, авторизацию, работу с PostgreSQL и медиафайлами, контейнеризацию и CI/CD.

## Возможности

- регистрация пользователей и токен-аутентификация;
- создание, просмотр, редактирование и удаление карточек котов;
- загрузка изображений в формате Base64;
- привязка достижений к карточкам;
- пагинация API;
- автоматические тесты, сборка Docker-образов и развёртывание через GitHub Actions.

## Стек

Python, Django, Django REST Framework, Djoser, PostgreSQL, React, Docker Compose, Nginx, GitHub Actions.

## Архитектура

- `backend/` — Django REST API и бизнес-логика;
- `frontend/` — клиент на React;
- `nginx/` — раздача статики, медиафайлов и проксирование запросов;
- `docker-compose.yml` — локальный запуск сервисов;
- `.github/workflows/main.yml` — тестирование, сборка образов и деплой.

Основные API-маршруты доступны по адресу `/api/`: `cats/`, `achievements/`, а также маршруты Djoser для пользователей и токенов.

## Локальный запуск

1. Клонируйте репозиторий и перейдите в его каталог.
2. Создайте файл `.env` на основе `.env.example` и задайте собственные значения.
3. Запустите сервисы:

```bash
docker compose up --build
```

После запуска приложение доступно на `http://localhost:9000`.

## Переменные окружения

```env
POSTGRES_DB=kittygram
POSTGRES_USER=kittygram_user
POSTGRES_PASSWORD=replace_with_a_strong_password
DB_HOST=db
DB_PORT=5432
SECRET_KEY=replace_with_a_long_random_value
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:9000
```

Настоящие секреты не должны попадать в Git: файл `.env` исключён через `.gitignore`, а CI/CD получает секреты из GitHub Actions Secrets.

## Проверки

Backend-проверки:

```bash
python -m flake8 backend/
cd backend
python manage.py test
```

Frontend-проверки:

```bash
cd frontend
npm ci
npm test -- --watchAll=false
```

GitHub Actions запускает проверки при каждом push в `main`. Публикация образов и деплой дополнительно требуют переменную репозитория `ENABLE_DEPLOY=true` и настроенные Actions Secrets; без неё внешние этапы безопасно пропускаются.

## Что демонстрирует проект

Проект подтверждает практику разработки REST API на Django REST Framework, моделирования связей в PostgreSQL, работы с аутентификацией, Docker Compose, Nginx и автоматизацией CI/CD.
