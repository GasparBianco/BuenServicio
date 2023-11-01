# Generated by Django 4.2.4 on 2023-11-01 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cashier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cashier_user', models.CharField(max_length=255)),
                ('open_money', models.PositiveIntegerField()),
                ('theorical_money', models.PositiveIntegerField()),
                ('close_money', models.PositiveIntegerField(blank=True)),
                ('open_date', models.DateTimeField(auto_now_add=True)),
                ('close_date', models.DateTimeField(blank=True)),
            ],
        ),
    ]
