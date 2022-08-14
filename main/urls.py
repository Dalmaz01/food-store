from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('foods', views.foods_page, name='foods_page'),
    path('login', views.login_page, name='login_page'),
    path('results_page', views.results_page, name='results_page'),
    path('food/<int:pk>', views.food_detail_page, name='food_detail_page'),
    path('profile', views.profile_page, name='profile_page'),
    path('profile/delete', views.profile_delete_view, name='delete_profile'),
    path('logout', views.logout_view, name='logout_view'),
    path('register', views.register_page, name='register_page'),
    path('contact_us', views.contact_us_page, name='contact_us_page'),
    path('history', views.history_page, name='history_page'),
    path('career', views.career_page, name='career_page'),
    path('business', views.business_page, name='business_page'),
    path('add_comment/<int:pk>', views.add_comment_view, name='add_comment'),
    path('add_rate/<int:pk>', views.add_rate_view, name='add_rate'),
]