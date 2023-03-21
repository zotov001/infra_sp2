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

Работа с API.

Получить список всех категорий

    http://127.0.0.1:8000/api/v1/categories/

Получить список всех жанров

    http://127.0.0.1:8000/api/v1/genres/

Получить список всех обьектов

    http://127.0.0.1:8000/api/v1/titles/

Получить список всех отзывов

    http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/

Комментарии к отзывам

    http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/

Получить список всех пользователей(доступно администратору)

    http://127.0.0.1:8000/api/v1/users/

Добавить нового пользователя(доступно администратору)

    http://127.0.0.1:8000/api/v1/users/

Самостоятельная регистрация на форуме пользователем. Получение JWT-токена.

    http://127.0.0.1:8000/api/v1/auth/signup/

    http://127.0.0.1:8000/api/v1/auth/token/

Автор сборки
Марк zotov001@yandex.ru
