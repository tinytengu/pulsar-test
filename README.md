# pulsar-test

Выполненное тестовое задание Pulsar (TEST_WORK-v2.pdf) на Django (Django REST Framework)

> Загружаемые файлы доступны по умолчанию только в Development режиме, в Production рекомендую использовать S3 хранилище.

## Запуск

```bash
# 1. Создать виртуальное окружение любым удобным способом

# 2. Активировать его и установить зависимости
pip install -r requirements.txt

# 3. Применить миграции
python3 manage.py makemigrations
python3 manage.py migrate

# 4. Создать аккаунт суперпользователя
python3 manage.py createsuperuser
```

### Development

```bash
# 5. Запустить в development режиме
python3 manage.py runserver
```

### Production

> Для запуска в Production рекомендуется использовать gunicorn / uvicorn / uwsgi
>
> Также, следует поменять переменную окружения `DJANGO_SETTINGS_MODULE` на `pulsar_test.settings_prod`

```bash
# 5. Запустить в production режиме
python3 -m uvicorn pulsar_test.asgi:application
```

## API

> Я считаю, что префикс `/api/` должен имплементироваться в Nginx, выступающем в качестве балансировщика нагруки / обратного прокси на микросервисы, поэтому в этом проекте эндпоинты `API` сделаны без него.

Документация в формате Swagger доступна по эндпоинту `/docs/`, Redoc по эндпоинту `/redoc`
![Документация Swagger](https://i.imgur.com/s1nYeX0.png)
