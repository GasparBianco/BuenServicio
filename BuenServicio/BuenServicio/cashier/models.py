from django.db import models

# Create your models here.
class Cashier(models.Model):

    cashier_user = models.CharField(max_length=255, blank=False, null=False)
    open_money = models.PositiveIntegerField(blank=False, null=False)
    theorical_money = models.PositiveIntegerField(blank=False, null=False)
    close_money = models.PositiveIntegerField(blank=True, null=True)
    open_date = models.DateTimeField(auto_now_add=True)
    close_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.open_date