from django.db import models

class ProductCategory(models.Model):

    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=255, blank=False, null=False)
    cost = models.IntegerField(blank=False, null=False)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name

