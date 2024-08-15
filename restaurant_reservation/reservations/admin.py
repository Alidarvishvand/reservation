from django.contrib import admin
from .models import Restaurant, Table, Reservation

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'opening_time', 'closing_time']

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['restaurant', 'table_number', 'seats']
    list_filter = ['restaurant']

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['customer_name','table','reservation_datetime']
    list_filter = ['table']
