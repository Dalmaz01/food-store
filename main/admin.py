from django.contrib import admin
from .models import(
    Category,
    Ratings,
    Foods,
    Comment,
    Orders
)

admin.site.register(Category)
admin.site.register(Ratings)
admin.site.register(Foods)
admin.site.register(Comment)
admin.site.register(Orders)
