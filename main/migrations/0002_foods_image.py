# Generated by Django 4.0.4 on 2022-07-27 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foods',
            name='image',
            field=models.ImageField(default=None, null=None, upload_to='', verbose_name='Image of food'),
        ),
    ]
