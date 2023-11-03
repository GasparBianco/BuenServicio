from django.db import models

# Create your models here.
class Cashier(models.Model):

    cashier_user = models.CharField(max_length=255, blank=False, null=False)
    open_money = models.PositiveIntegerField(blank=False, null=False)
    theorical_money = models.PositiveIntegerField(blank=False, null=False)
    total_sold = models.PositiveIntegerField(blank=False, null=False, default=0)
    close_money = models.PositiveIntegerField(blank=True, null=True)
    open_date = models.DateTimeField(auto_now_add=True)
    close_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.open_date
    
class History(models.Model):

    price = models.PositiveIntegerField(blank=False, null=False)
    table = models.IntegerField(blank=False, null=False)
    payment_method = models.CharField(max_length=255, blank=False, null=False)
    date = models.DateTimeField(blank=True, null=True)