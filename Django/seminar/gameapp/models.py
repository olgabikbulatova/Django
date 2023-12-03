from django.db import models
from django.utils import timezone

# Create your models here.


class Headtails(models.Model):
    result = models.CharField(max_length=20)
    result_time = models.DateTimeField(default=timezone.now)

    @staticmethod
    def values():
        value = Headtails.objects.order_by('-result_time')[:5]
        # print(value)
        return value

    def __str__(self):
        return f'side {self.result} time {self.result_time}'
