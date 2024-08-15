from django import forms
from .models import Reservation, Table

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table','restaurant' ,'customer_name','reservation_datetime']
        widgets = {
            'reservation_time': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

    def __init__(self, *args, **kwargs):
        restaurant = kwargs.pop('restaurant', None)
        super().__init__(*args, **kwargs)
        if restaurant:
            self.fields['table'].queryset = Table.objects.filter(restaurant=restaurant)
