from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def recipes(request):
    return HttpResponse('Список рецептов')


def recipes_detail(request):
    return HttpResponse('Рецепт подробно')


def download_shopping_cart(request):
    return HttpResponse('Скачать рецепт')


def shopping_cart(request):
    return HttpResponse('Список покупок по рецепту')


def favorite(request):
    return HttpResponse('Избранное')
