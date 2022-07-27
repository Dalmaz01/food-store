from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='category')

    def __str__(self):
        return self.name


class Ratings(models.Model):
    number = models.IntegerField(default=0, verbose_name='number of rate')

    def __str__(self):
        return f"{self.number} star"


class Foods(models.Model):
    name = models.CharField(max_length=100, verbose_name='name of food')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(default=0, verbose_name='price of food')
    description = models.TextField(verbose_name='description')
    rating = models.ForeignKey(Ratings, on_delete=models.PROTECT)
    image = models.ImageField(verbose_name='Image of food', default=None, null=None)

    def __str__(self):
        return self.name


