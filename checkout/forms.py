from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (          
            'name',            
            'email',
            'phone_number', 
            'country', 
            'postcode',
            'address_line1',
            'address_line2', 
            'town_or_city', 
            'state_or_county',
            )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {                           
            'name': 'Name',            
            'email': 'Email',
            'phone_number': 'Phone Number',             
            'postcode': 'Postcode',
            'address_line1': 'Address 1',
            'address_line2': 'Address 2', 
            'town_or_city': 'Town or City', 
            'state_or_county': 'State or County',
            }

        self.fields['name'].widget.attrs['autofocus'] = True          
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
                self.fields[field].label = False