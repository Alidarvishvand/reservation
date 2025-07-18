from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('booktable/', views.booktable, name='booktable'),
    path('reservation/', views.reserve, name='reserve'),
    path('reserve/<int:restaurant_id>/', views.reservation_view, name='reserve'),
    path('success/', views.success, name='success'),
]
