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
                    'original_shoppingcart',
                    'stripe_pid',
                    'member_discount',
                    )

    fields = (
                'order_number',
                'user_profile',
                'name',
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
                'member_discount',
                'order_total',
                'grand_total',
                'original_shoppingcart',
                'stripe_pid',
                )

    list_display = (
                    'order_number',
                    'name',
                    'email',
                    'phone_number',
                    'country',
                    'postcode',
                    'address_line1',
                    'address_line2',
                    'town_or_city',
                    'state_or_county',
                    'date',
                    'member_discount',
                    'delivery_cost',
                    'order_total',
                    'grand_total',
                    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
