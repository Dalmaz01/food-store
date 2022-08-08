from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')

    def __str__(self):
        return self.name


class Ratings(models.Model):
    number = models.IntegerField(default=0, verbose_name='Звезды рейтинга')

    def __str__(self):
        return f"{self.number} star"


class Foods(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название еды')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(default=0, verbose_name='Цена еды')
    description = models.TextField(verbose_name='Описание')
    rating = models.ForeignKey(Ratings, on_delete=models.PROTECT)
    image = models.ImageField(verbose_name='Фотография продукта', default=None, null=None)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.CharField(max_length=30, verbose_name='Автор комментария')
    comment_text = models.TextField(verbose_name='Текст комментария')
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата создания комментария')
    food = models.ForeignKey(Foods, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}: {self.created_date} - {self.food}"
# class Wishlist(models.Model):
#     food = models.ManyToManyField
#     count = models.IntegerField(default=0, verbose_name='Количество продукта')

# class Orders(models.Model):
#     food = models.ManyToManyField(Foods)
#     date_time = models.DateTimeField(auto_now_add=True)
#     count = models.IntegerField()
