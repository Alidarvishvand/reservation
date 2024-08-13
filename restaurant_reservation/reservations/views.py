from django.shortcuts import render, redirect,get_object_or_404
from .models import Restaurant, Reservation
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

@login_required
def reserve(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('success')  
    else:
        form = ReservationForm()
    return render(request, 'reserve.html', {'form': form})

def success(request):
    return render(request, 'success.html')