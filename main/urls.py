from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('home', views.home_page, name='home_page'),
    path('foods', views.foods_page, name='foods_page'),
    path('login', views.login_page, name='login_page'),
]