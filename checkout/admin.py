from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    
    readonly_fields = (
                    'order_number',
                    'date',
                    'delivery_cost',
                    'order_total',
                    'grand_total',
                    )                    

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

    list_display = (
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

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)    