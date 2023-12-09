from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from random import randint, choice
import logging
from datetime import timedelta, datetime

from django.utils import timezone
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
    order_t = Order(customer_id=5)
    order_t.save()
    t_price = 0
    for y in range(1, 5):
        prod = Product.objects.get(pk=y)
        order_t.products.add(prod)
        t_price += prod.price
        order_t.total_price = t_price
    return HttpResponse('fffffff')


def client_order(request, client_id):
    name = Client.objects.filter(pk=client_id).first()
    orders = name.order_set.all()
    context = {'name': name, 'orders': orders}
    return render(request, 'shopapp/cl_order.html', context)


def client_product(request, client_id):
    name = Client.objects.filter(pk=client_id).first()
    orders = name.order_set.all()
    week_prod=set()
    month_prod=set()
    year_prod=set()
    now = timezone.now()
    for order in orders:
        products = order.products.all()
        delta = now - order.date_ordered
        if delta.days<=7:
            for product in products:
                week_prod.add(product)
        elif delta.days<=30:
            for product in products:
                month_prod.add(product)
        elif delta.days<=365:
            for product in products:
                year_prod.add(product)
    context = {'name': name, 'w_prod': week_prod, 'm_prod': month_prod, 'y_prod': year_prod}
    return render(request, 'shopapp/cl_product.html', context)

