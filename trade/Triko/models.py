from datetime import timezone

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class color(models.Model):
    name = models.CharField(max_length=10)
    image = models.ImageField(upload_to='color/')
    def __str__(self):
        return self.name

class Triko_Model(models.Model):
    name = models.CharField(max_length=10)
    SIZE = (('sm', 'small'), ('md', 'meduim'), ('lg', 'large'))
    size = models.CharField(choices=SIZE, max_length=2)
    image = models.ImageField(upload_to='media/image')
    date = models.DateField(auto_now=True)
    description = models.TextField(max_length=100)
    price = models.PositiveSmallIntegerField(default=150)
    like = models.PositiveIntegerField(default=0)
    colors = models.ManyToManyField(color)
    def __str__(self):
        return self.name


class imag(models.Model):
    image = models.ImageField(upload_to='image')
class Trader(models.Model):
    name = models.CharField(max_length=20, default='غير موجود')
    model_define = models.ForeignKey(Triko_Model, on_delete=models.CASCADE, )
    telephone = models.CharField(max_length=11)
    email_facebook = models.CharField(max_length=30)
    address = models.CharField(max_length=40)
    quentity = models.IntegerField()

    def __str__(self):
        return self.model_define.name
