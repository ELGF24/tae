from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('about-us/', views.about_us, name='about-us'),
]