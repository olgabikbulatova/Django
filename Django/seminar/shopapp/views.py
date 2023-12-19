from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.db.models import Sum
# Create your views here.
from django.http import HttpResponse
from random import randint, choice
import logging
from datetime import timedelta, datetime

from django.utils import timezone
from unicodedata import decimal

from .models import Client, Product, Order
from .forms import ProdEditForm

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


def update_product(request, id):
    ed_product = Product.objects.get(pk=id)
    if ed_product is not None:
        if request.method == 'POST':
            form = ProdEditForm(request.POST, request.FILES)
            if form.is_valid():
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']
                price = form.cleaned_data['price']
                quantity = form.cleaned_data['quantity']
                image = form.cleaned_data['image']
                fs = FileSystemStorage()
                fs.save(image.name, image)
                ed_product.name = name
                ed_product.description = description
                ed_product.price = price
                ed_product.quantity = quantity
                ed_product.image = image
                ed_product.save()
                return HttpResponse(f'new data')
        else:
            form = ProdEditForm(instance=ed_product)
            context = {'form': form, 'product': ed_product}
            return render(request, "shopapp/prodedit.html", context)


def total_in_view(request):
    products = Product.objects.all()
    total = sum(product.quantity for product in products)
    context = {
        'title': 'Общее количество посчитано в представлении',
        'total': total,
    }
    return render(request, 'shopapp/total_count.html', context)


def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
        'title': 'Общее количество посчитано в базе данных',
        'total': total,
    }
    return render(request, 'shopapp/total_count.html', context)


def total_in_template(request):
    context = {
        'title': 'Общее количество посчитано в шаблоне',
        'products': Product,
    }
    return render(request, 'shopapp/total_count.html', context)


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

