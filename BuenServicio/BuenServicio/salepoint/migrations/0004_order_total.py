# Generated by Django 4.2.4 on 2023-10-31 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salepoint', '0003_alter_order_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.PositiveIntegerField(default=1000),
            preserve_default=False,
        ),
    ]
