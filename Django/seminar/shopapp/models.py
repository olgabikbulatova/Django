from django.db import models
from django.utils import timezone

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    reg_day = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}, regday:{self.reg_day}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    quantity = models.IntegerField()
    add_day = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()

    def __str__(self):
        return f'Product: {self.name}, price:{self.price}'


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, null=True)

    def __str__(self):
        return (f'New order: customer name {self.customer.name},'
                f' items: {" ".join(str(name) for name in self.products.all())},'
                f' total order price:{self.total_price}')
