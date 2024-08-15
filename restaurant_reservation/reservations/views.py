from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant, Reservation, Table
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.utils import timezone
def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'index.html', {'restaurants': restaurants}) 

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def booktable(request):
    if request.method == 'POST':
        return render(request, 'success.html')  
    return render(request, 'book.html')

@login_required
def reserve(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            try:
                reservation.save()
                return redirect('success')  
            except ValidationError as e:
                form.add_error(None, e.message)
    else:
        form = ReservationForm()
    return render(request, 'reserve.html', {'form': form})

@login_required
def reservation_view(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            table = form.cleaned_data['table']
            reservation_datetime = form.cleaned_data['reservation_datetime']

           
            existing_reservations = Reservation.objects.filter(
                table=table,
                reservation_datetime__date=reservation_datetime.date()
            )

            if existing_reservations.filter(
                reservation_datetime__time__gte=reservation_datetime.time() - timezone.timedelta(minutes=30),
                reservation_datetime__time__lt=reservation_datetime.time() + timezone.timedelta(minutes=30)
            ).exists():
                form.add_error(None, "این میز در زمان انتخابی برای این رستوران قبلاً رزرو شده است.")
            else:
                reservation = form.save(commit=False)
                reservation.restaurant = restaurant
                reservation.user = request.user
                reservation.save()
                return redirect('success')  
    else:
        form = ReservationForm()

    return render(request, 'reserve.html', {'form': form, 'restaurant': restaurant})
def success(request):
    return render(request, 'success.html')
