from django.urls import path
from main import views as main_views

app_name = 'manager'

urlpatterns = [
    path('profile', main_views.profile_page, name='profile_page'),
]