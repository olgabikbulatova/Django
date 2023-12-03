from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from random import randint, choice
import logging

from unicodedata import decimal

from .models import Client, Product, Order

logger = logging.getLogger(__name__)


def index(request):
    html = """
        <h1>Привет,  это магазин</h1>
    """
    logger.info('Index page accessed')
    return HttpResponse(html)


def client(request):
    for i in range(10):
        client_test = Client(name=f'aaa{i}', email=f'aaa@rt{i}.ru', phone=f'1234565{i}', address=f'bbb{i}')
        client_test.save()
    return HttpResponse('client')


def add_client(request):
    new_client = Client(name=f'arggaegr', email=f'xxxxx@rt.ru', phone=f'000000', address=f'bbbadfsdgsfg')
    new_client.save()
    return HttpResponse(f'add new client {new_client}')


def del_client(request, id):
    user = Client.objects.filter(pk=id).first()
    if user is not None:
        user.delete()
        return HttpResponse(f'client {user} deleted')


def update_client(request, id):
    name = 'Olga'
    user = Client.objects.filter(pk=id).first()
    if user is not None:
        user.name = name
        user.save()
        return HttpResponse(f'client {user} name changed')


def find_client(request, id):
    user = Client.objects.filter(pk=id).first()
    if user is not None:
        return HttpResponse(f'client {user} ')


def product(request):
    for i in range(10):
        product_t = Product(name=f'aaa{i}', description=f'bbbbbb{i}', price=100.000, quantity=f'1{i}')
        product_t.save()
    return HttpResponse('product')


def order(request):
    return HttpResponse('order')


def new_order(request):
    order_t = Order(customer_id=1)
    order_t.save()
    t_price = 0
    for i in range(1, 5):
        prod = Product.objects.get(pk=i)
        order_t.products.add(prod)
        t_price += prod.price
        order_t.total_price = t_price
    return HttpResponse(f'{order_t}')
