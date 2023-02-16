from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index/', views.index, name = 'index'),
    path('generate_random_num/', views.generate_random_num, name = 'generate_random_num'),
    path('test_number/', views.test_number, name = 'test_number'),
   
]