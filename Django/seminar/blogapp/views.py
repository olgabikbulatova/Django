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
            bday='1900-01-19'
        )
        lst.append(autr)
        autr.save()
    return HttpResponse(lst)


def post(request):
    for i in range(10):
        for y in range(5):
            post = Post(
                title=f'aaa{y+1}',
                content=f'xxxx xxxx{y}',
                author_id=i + 1,
            )
            post.save()
    return HttpResponse('post')


def a_post(request, author_id):
    name = Author.objects.filter(pk=author_id).first()
    posts = name.post_set.all()
    context = {'name': name, 'posts': posts}
    return render(request, 'blogapp/a_post.html', context)