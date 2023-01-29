from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField()
    rate = models.FloatField()
