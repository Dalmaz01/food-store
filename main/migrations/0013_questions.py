# Generated by Django 4.0.4 on 2022-08-10 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_orders_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('phone_number', models.IntegerField(verbose_name='Номер телефона')),
                ('email', models.CharField(max_length=50, verbose_name='Адрес эл. почты')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')),
            ],
        ),
    ]
