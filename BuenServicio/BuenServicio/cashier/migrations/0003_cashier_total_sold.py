# Generated by Django 4.2.4 on 2023-11-03 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashier', '0002_alter_cashier_close_date_alter_cashier_close_money'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashier',
            name='total_sold',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
