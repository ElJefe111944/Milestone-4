from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    shoppingcart = request.session.get('shoppingcart', {})
    if not shoppingcart:
        messages.error(
            request, "There is nothing currently in your shopping bag")
        return redirect(reverse('watches'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51ISpcuFD3z975eMdp4FlRPhOi294WwDqphFoj8pPdEpPhMDSVAgJT20HfabXRbIX0B94XA0rrUlktKJxFJ918mVg00sIuBIT5a',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)