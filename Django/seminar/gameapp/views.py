from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from random import randint, choice
import logging
from .models import Headtails


logger = logging.getLogger(__name__)


def index(request):
    html = """
        <h1>Привет,  в этом разделе будут храниться игры</h1>
        <p>в некоторые из них можно поиграть уже сейчас:</p>
        <ul>
        <li><a href='headtails'>Орел и решка</a></li>
        <li><a href='cubes'>Кости</a></li>
        <li><a href='hundred'>Отгадай число</a></li>
        </ul>
        <br><a href='about'>подробнее обо мне.</a>
    """
    logger.info('Index page accessed')
    return HttpResponse(html)


def about(request):
    html = """
        <h1>Это проект в рамках семинаров курса по Django</h1>
        <p>Меня зовут Оля, я люблю:</p>
        <ul>
        <li>блаблабла</li>
        <li>блаблабла</li>
        <li>блаблабла</li>
        </ul>
        <br/><a href='/game'>На главную.</a>
    """
    logger.info('About page accessed')
    return HttpResponse(html)


def head_tails(request):
    side = choice(["Head","Tail"])
    coin = Headtails(result=side)
    coin.save()
    return HttpResponse(f'Поздравляю! у вас {side}')


def headtails_values(request):
    value = Headtails.values()
    lst = list(i.result for i in value)
    count_h = 0
    count_t = 0
    for i in lst:
        if i == 'Head':
            count_h += 1
        else: count_t += 1
    return HttpResponse(f'Статистика последних пяти бросков "Head"  выпало {count_h} раз, "Tail" -  {count_t} ')


def cubes(request):
    return HttpResponse(f'{randint(1,6)}')


def hundred(request):
    return HttpResponse(f'{randint(0,100)}')
