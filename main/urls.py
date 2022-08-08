from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('home', views.home_page, name='home_page'),
    path('foods', views.foods_page, name='foods_page'),
    path('login', views.login_page, name='login_page'),
    path('results_page', views.results_page, name='results_page'),
    path('food/<int:pk>', views.food_detail_page, name='food_detail_page'),
    path('profile', views.profile_page, name='profile_page'),
    path('profile/delete', views.profile_delete_view, name='delete_profile'),
    path('logout', views.logout_view, name='logout_view'),
    path('register', views.register_page, name='register_page'),
]