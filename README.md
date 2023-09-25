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

______________
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
**POST | Создание рецепта: http://127.0.0.1:8000/api/recipes/**

```{
  "ingredients": [
    {
      "id": 1123,
      "amount": 10
    }
  ],
  "tags": [
    1,
    2
  ],
  "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==",
  "name": "string",
  "text": "string",
  "cooking_time": 1
}```


______________
## Доступ к сайту:
Сайт доступен по адресу https://karkyshka.ddns.net
Данные для вода в админку:
- admin@admin.ru
- admin
