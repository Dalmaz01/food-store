# Generated by Django 4.0.4 on 2022-08-09 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_orders_food_orders_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='price',
            field=models.IntegerField(default=None, null=None, verbose_name='Сумма'),
        ),
    ]
