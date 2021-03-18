from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from watches.models import Watch


def shoppingcart_contents(request):

    shoppingcart_items = []
    total = 0
    product_count = 0
    shoppingcart = request.session.get('shoppingcart', {})

    for item_id, quantity in shoppingcart.items():
        watch = get_object_or_404(Watch, pk=item_id)
        total += quantity * watch.price
        product_count += quantity
        shoppingcart_items.append({
            'item_id': item_id, 
            'quantity': quantity,
            'watch': watch,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0 
        free_delivery_delta = 0

    discount = total * Decimal(settings.MEMBER_DISCOUNT / 100)

    if request.user.is_authenticated:
        grand_total = total - discount + delivery

    else:
        grand_total = total + delivery
    context = {
        'shoppingcart_items': shoppingcart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'discount': discount,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }
    
    return context