from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index/', views.index, name = 'index'),
    path('generate_random_num/', views.generate_random_num, name = 'generate_random_num'),
    path('test_number/', views.test_number, name = 'test_number'),
    path('exit/', views.exit, name = 'exit'),
    path('or_lotto/', views.or_lotto, name = 'or_lotto'),
    path('get_lotto_results/', views.get_lotto_results, name = 'get_lotto_results'),
    path('generate_powerball/', views.generate_powerball, name = 'generate_powerball'),
    path('generate_megamill/', views.generate_megamill, name = 'generate_megamill'),
    path('test_powerball/', views.test_powerball, name = 'test_powerball'),
    path('test_megamill/', views.test_megamill, name = 'test_megamill'),
    path('generate_luckylines/', views.generate_luckylines, name = 'generate_luckylines'),
    path('test_luckylines/', views.test_luckylines, name = 'test_luckylines'),
    path('contact/', views.contact, name = 'contact'),
    path('success/', views.success, name = 'success'),
]