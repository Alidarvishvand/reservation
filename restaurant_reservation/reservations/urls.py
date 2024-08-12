from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurant/<int:pk>/', views.restaurant_detail, name='restaurant_detail'),
    path('restaurant/<int:pk>/reserve/', views.make_reservation, name='make_reservation'),
    path('reservation-success/', views.reservation_success, name='reservation_success'),
]
