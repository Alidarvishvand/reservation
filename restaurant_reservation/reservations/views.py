from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant, Reservation, Table
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError

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
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            table = form.cleaned_data['table']
            reservation_date = form.cleaned_data['reservation_date']
            time_slot = form.cleaned_data['time_slot']

            # بررسی اینکه آیا این میز در تاریخ و زمان مشخص رزرو شده است
            existing_reservation = Reservation.objects.filter(
                table=table,
                reservation_date=reservation_date,
                time_slot=time_slot
            ).exists()

            if existing_reservation:
                form.add_error(None, "This table is already reserved for the selected date and time.")
            else:
                form.save()
                return redirect('success_url')  # تغییر به URL موفقیت خودتان
    else:
        form = ReservationForm()

    return render(request, 'reservation_template.html', {'form': form})

def success(request):
    return render(request, 'success.html')
