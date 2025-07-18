# FastAPI Notes Application

Простое приложение для управления заметками с использованием FastAPI, PostgreSQL и Redis.

## Технологии

- **FastAPI** - веб-фреймворк
- **PostgreSQL** - основная база данных
- **Redis** - кэширование и Celery брокер
- **SQLModel** - ORM
- **Celery** - асинхронные задачи
- **Docker** - контейнеризация

## CI/CD Pipeline

Проект настроен с автоматическим CI/CD пайплайном через GitHub Actions.

### Что делает пайплайн:

1. **Запускается при**: push в ветки `main` или `master`, а также при pull request
2. **Проверяет код**: запускает все тесты с PostgreSQL и Redis
3. **Собирает Docker образ**: создает образ приложения
4. **Тестирует образ**: проверяет, что приложение запускается корректно
5. **Сохраняет артефакты**: загружает результаты тестов

### Шаги пайплайна:

- ✅ Checkout code
- ✅ Setup Python 3.10
- ✅ Install dependencies
- ✅ Setup PostgreSQL и Redis services
- ✅ Run tests
- ✅ Build Docker image
- ✅ Test Docker image
- ✅ Upload test results

## Локальная разработка

### Запуск с Docker Compose:

```bash
docker-compose up --build
```

### Запуск тестов локально:

```bash
pytest tests/ -v
```

### Запуск без Docker:

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Настройте переменные окружения (создайте файл `.env`):
```env
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/user
REDIS_URL=redis://localhost:6379
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

3. Запустите PostgreSQL и Redis

4. Запустите приложение:
```bash
uvicorn main:app --reload
```

## API Endpoints

- `GET /docs` - Swagger документация
- `POST /auth/register` - регистрация пользователя
- `POST /auth/login` - авторизация
- `GET /notes/` - получение заметок
- `POST /notes/` - создание заметки
- `PUT /notes/{note_id}` - обновление заметки
- `DELETE /notes/{note_id}` - удаление заметки

## Структура проекта

```
├── .github/workflows/    # CI/CD конфигурация
├── auth/                 # Аутентификация
├── notes/                # Модуль заметок
├── tests/                # Тесты
├── main.py              # Основное приложение
├── database.py          # Настройки БД
├── models.py            # Модели данных
├── requirements.txt     # Зависимости Python
├── Dockerfile          # Docker конфигурация
└── docker-compose.yml  # Docker Compose
``` 