from django.contrib import admin
from .models import(
    Category,
    Foods,
    Comment,
    Orders,
    Questions,
    Career,
    Rating
)

admin.site.register(Category)
admin.site.register(Foods)
admin.site.register(Comment)
admin.site.register(Orders)
admin.site.register(Questions)
admin.site.register(Career)
admin.site.register(Rating)
