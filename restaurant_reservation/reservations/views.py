from django.shortcuts import render, redirect,get_object_or_404
from .models import Restaurant, Reservation,Table
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required


def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'index.html', {'restaurants': restaurants}) 


def restaurant_detail(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    return render(request, 'resturant_detail.html', {'restaurant': restaurant}) 


@login_required
def make_reservation(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    tables = Table.objects.filter(restaurant=restaurant)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_success')
    else:
        form = ReservationForm()

    return render(request, 'make_reservation.html', {'form': form, 'restaurant': restaurant, 'tables': tables})



def reservation_success(request):
    return render(request, 'reservation_success.html')