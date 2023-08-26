from django.db import models

class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)
    available = models.BooleanField(default=True)
    last_order = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Table {self.number}"
