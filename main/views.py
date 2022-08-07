from django.shortcuts import render
from . import models


def foods_page(request):
    all_foods = models.Foods.objects.all()

    context = {
        'all_foods': all_foods,

    }
    return render(request, 'main/foods.html', context)


def login_page(request):
    return render(request, 'main/login.html', {})


def home_page(request):
    return render(request, 'main/home.html', {})

