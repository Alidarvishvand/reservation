from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name


class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table_number = models.IntegerField()
    seats = models.CharField(max_length=20)

    def __str__(self):
        return f"Table {self.table_number} ({self.seats} seats)"


class Reservation(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)
    table = models.ForeignKey(Table, related_name='reservations', on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    reservation_time = models.DateField(default=timezone.now)  
    time_slot = models.TimeField(default='12:00')
    def clean(self):
        if Reservation.objects.filter(
            table=self.table, 
            reservation_time=self.reservation_time
        ).exists():
            raise ValidationError('این میز در زمان انتخابی برای این رستوران قبلاً رزرو شده است.')

    def save(self, *args, **kwargs):
        self.clean()  
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('table', 'reservation_time')

    def __str__(self):
        restaurant_name = self.restaurant.name if self.restaurant else "Unknown Restaurant"
        return f"Reservation for {self.customer_name} at {restaurant_name} on {self.reservation_time}"
