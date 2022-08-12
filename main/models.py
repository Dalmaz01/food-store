from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')

    def __str__(self):
        return self.name





class Foods(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название еды')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(default=0, verbose_name='Цена еды')
    description = models.TextField(verbose_name='Описание')
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


class Orders(models.Model):
    food = models.ForeignKey(Foods, on_delete=models.CASCADE, default=None, null=None)
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    phone_number = models.IntegerField(verbose_name='Номер телефона')
    address = models.CharField(max_length=150, verbose_name='Адрес')
    food_count = models.IntegerField(verbose_name='Кол-во', default=None, null=None)
    price = models.IntegerField(verbose_name='Сумма', default=None, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Время заказа', null=None)

    def __str__(self):
        return f"{self.food}: {self.first_name} {self.last_name} - {self.date}"


class Questions(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    phone_number = models.IntegerField(verbose_name='Номер телефона')
    email = models.CharField(max_length=50, verbose_name='Адрес эл. почты')
    message = models.TextField(verbose_name='Сообщение')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')

    def __str__(self):
        return f"{self.first_name}: {self.message}"


class Career(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    email = models.CharField(max_length=100, verbose_name='Адрес эл. почты')
    stuff = models.CharField(max_length=100, verbose_name='Желаемая должность')
    resume = models.FileField(upload_to='MEDIA_ROOT', verbose_name='Резюме')
    message = models.TextField(verbose_name='Сопроводительное письмо')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')

    def __str__(self):
        return f"{self.full_name}: {self.resume}"