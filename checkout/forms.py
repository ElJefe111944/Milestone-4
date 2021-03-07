from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        fields = (
            'order_number', 
            'first_name',
            'last_name', 
            'email',
            'phone_number', 
            'country', 
            'postcode',
            'address_line1',
            'address_line2', 
            'town_or_city', 
            'state_or_county',
            'date', 
            'delivery_cost',
            'order_total', 
            'grand_total', 
            )