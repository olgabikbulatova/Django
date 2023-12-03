from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from random import randint, choice
import logging
from .models import Author, Post


logger = logging.getLogger(__name__)


def index(request):
    html = """
        <h1>Привет,  в этом разделе будут храниться статьи</h1>
        <p>в много авторов и интересные темы:</p>
    """
    logger.info('Index page accessed')
    return HttpResponse(html)


def author(request):
    lst = []
    for i in range(10):
        autr = Author(
            name=f'AAA {i}',
            lastname=f'AAA {i}',
            email=f'{i}@aaa.ru',
            bio=f'AAA {i}',
            bday='01.01.1900'
        )
        lst.append(autr)
    return HttpResponse(lst)


def post(request):
    return HttpResponse('post')
