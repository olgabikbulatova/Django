from django.db import models
from django.utils import timezone


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(max_length=1000)
    bday = models.DateField()

    def full_name(self):
        return f'{self.name} {self.lastname}'

    def __str__(self):
        return f'Name: {self.full_name()}, email: {self.email}'


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    add_data = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    vws = models.IntegerField(default=0)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'Title is {self.title}'
