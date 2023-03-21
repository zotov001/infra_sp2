REST API проект для сервиса YaMDb собирает отзывы пользователей на произведения, 
на основе оценок рассчитывается рейтинг произведения. 
Можно оставлять комментарии к отзывам других пользователей.

Технологии

    Python 3.7, Django 2.2.19, Gunicorn 20.0.4, Docker, NGINX, PostgresSQL

Запуск docker-compose(из папки с docker-compose.yaml)

    docker-compose up -d --build
    
Выполните миграции:

    docker-compose exec backend python manage.py migrate
    
Создайте суперпользователя:

    docker-compose exec backend python manage.py createsuperuser
    
Соберите статику:

    docker-compose exec backend python manage.py collectstatic --no-input

Документация API YaMDb доступна по эндпойнту: 

    http://localhost/redoc/

Автор сборки
Марк zotov001@yandex.ru
