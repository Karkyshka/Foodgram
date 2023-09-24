# Фильный учебный проект
## Кулинарный сайт

Проектом «Фудграм» — сайт, на котором пользователи публикуют рецепты,
добавляют чужие рецепты в избранное и подписываются на публикации других авторов.
Пользователям сайта также доступен сервис «Список покупок».
Он позволит создавать список продуктов, которые нужно купить для приготовления
выбранных блюд.

___________

## Технологии в проекте:
- Python
- Django
- Django REST framework
- Nginx
- Docker
- Postgres
# Фильный учебный проект
## Кулинарный сайт

Проектом «Фудграм» — сайт, на котором пользователи публикуют рецепты,
добавляют чужие рецепты в избранное и подписываются на публикации других авторов.
Пользователям сайта также доступен сервис «Список покупок».
Он позволит создавать список продуктов, которые нужно купить для приготовления
выбранных блюд.

______________

## Технологии в проекте:
- Python
- Django
- Django REST framework
- Nginx
- Docker
- Postgres
______________
## Для запуска проекта:
- Клонируйте репозиторий:

git clone https://github.com/Karkyshka/foodgram-project-react.git
- Установите и активируйте виртуальное окружение:

python -m venv venv
source venv/bin/activate
source venv/Scripts/activate

- Установите зависимости из файла requirements.txt:
pip install -r requirements.txt

- Примените миграции:
python manage.py migrate

- В папке с файлом manage.py выполните команду для запуска локально:

python manage.py runserver


### Собираем контейнеры:
- Разверните контейнеры при помощи docker-compose:
docker-compose up -d --build

- Выполните миграции:
docker-compose exec backend python manage.py migrate

- Создайте суперпользователя:
docker-compose exec backend python manage.py createsuperuser

- Соберите статику:
docker-compose exec backend python manage.py collectstatic 

- Остановка проекта:
docker-compose down

______________
## Примеры апи запросов и ответов:



______________
## Доступ к сайту:
Сайт доступен по адресу https://karkyshka.ddns.net
Данные для вода в админку:
- admin@admin.ru
- admin