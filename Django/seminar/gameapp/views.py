from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from random import randint, choice
import logging

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
    return HttpResponse(f'{choice(["Head","Tail"])}')


def cubes(request):
    return HttpResponse(f'{randint(1,6)}')


def hundred(request):
    return HttpResponse(f'{randint(0,100)}')
