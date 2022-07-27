from django.shortcuts import render
from . import models


def home_page(request):
    all_foods = models.Foods.objects.all()
    return render(request, 'main/home.html', {'all_foods': all_foods})