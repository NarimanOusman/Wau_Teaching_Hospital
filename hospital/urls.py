from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('appointment/', views.appointment, name='appointment'),
    path('services/', views.services, name='services'),
    path('doctors/', views.doctors, name='doctors'),
    path('accident_report/', views.accident_report, name='accident_report'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]