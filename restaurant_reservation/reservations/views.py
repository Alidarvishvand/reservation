from django.shortcuts import render, redirect,get_object_or_404
from .models import Restaurant, Reservation,Table
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required


def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'index.html', {'restaurants': restaurants}) 


def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def booktable(request):
    if request.method == 'POST':
        return render(request, 'thankyou.html')  
    return render(request, 'book.html')