from django.db import models

# Create your models here.
from django.db import models

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
    seats = models.IntegerField()

    def __str__(self):
        return f"Table {self.table_number} ({self.seats} seats)"

class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    reservation_time = models.DateTimeField()

    def __str__(self):
        return f"Reservation for {self.customer_name} on {self.reservation_time}"
