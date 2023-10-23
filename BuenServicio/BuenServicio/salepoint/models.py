from django.db import models
from products.models import Product
from tables.models import Table

# Create your models here.
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)