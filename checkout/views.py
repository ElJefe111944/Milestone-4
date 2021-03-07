from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    shoppingcart = request.session.get('shoppingcart', {})
    if not shoppingcart:
        messages.error(request, "There is nothing currently in your shopping bag")
        return redirect(reverse('watches'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)