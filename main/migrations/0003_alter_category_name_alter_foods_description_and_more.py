# Generated by Django 4.0.4 on 2022-08-07 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_foods_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='foods',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='foods',
            name='image',
            field=models.ImageField(default=None, null=None, upload_to='', verbose_name='Фотография продукта'),
        ),
        migrations.AlterField(
            model_name='foods',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название еды'),
        ),
        migrations.AlterField(
            model_name='foods',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена еды'),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='number',
            field=models.IntegerField(default=0, verbose_name='Звезды рейтинга'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30, verbose_name='Автор комментария')),
                ('comment_text', models.TextField(verbose_name='Текст комментария')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Дата создания комментария')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.foods')),
            ],
        ),
    ]