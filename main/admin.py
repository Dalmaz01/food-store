from django.contrib import admin
from .models import(
    Category,
    Ratings,
    Foods
)

admin.site.register(Category)
admin.site.register(Ratings)
admin.site.register(Foods)
