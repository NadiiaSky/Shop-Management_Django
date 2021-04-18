from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.
class Shop(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500)
    imageUrl = models.CharField(max_length=150)


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)


class Product(models.Model):
    # description = models.CharField(max_length=500)
    description = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True)
    # description_category = models.ManyToManyField(Category, db_column='title')
    product_title = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    price = models.FloatField(default=0.00)
    images = models.CharField(max_length=150)
    active = models.BooleanField(default=False)
