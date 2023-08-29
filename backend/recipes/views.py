from django.http import HttpResponse
from .models import *
from django.shortcuts import render
from rest_framework import viewsets


def RecipViewSet(viewsets.ModelViewSet):
    return HttpResponse('Список рецептов')


def recipes_detail(request):
    return HttpResponse('Рецепт подробно')


def download_shopping_cart(request):
    return HttpResponse('Скачать рецепт')


def shopping_cart(request):
    return HttpResponse('Список покупок по рецепту')


def favorite(request):
    return HttpResponse('Избранное')
