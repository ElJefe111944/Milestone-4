from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.contrib import messages

from watches.models import Watch

# Create your views here.


def view_shoppingcart(request):
    """  A view to render the shopping cart  """
    
    return render(request, 'shoppingcart/shoppingcart.html')


def add_to_shoppingcart(request, item_id):
    """ Add a quantity of a specified product to the shopping bag """

    watch = get_object_or_404(Watch, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shoppingcart = request.session.get('shoppingcart', {})

    if item_id in list(shoppingcart.keys()):
        shoppingcart[item_id] += quantity
        messages.success(
            request, f'Updated {watch.name} quantity to the {shoppingcart[item_id]}')
    else:
        shoppingcart[item_id] = quantity
        messages.success(request, f'Added {watch.name} to the shopping cart')

    request.session['shoppingcart'] = shoppingcart
    return redirect(redirect_url)


def update_shoppingcart(request, item_id):
    """ Update the quantity of a specified product to the shopping bag """

    watch = get_object_or_404(Watch, pk=item_id)
    quantity = int(request.POST.get('quantity')) 
    shoppingcart = request.session.get('shoppingcart', {})

    if quantity > 0:
        shoppingcart[item_id] = quantity
        messages.success(
            request, f'Updated {watch.name} quantity to {shoppingcart[item_id]}')
        
    else:
        shoppingcart.pop(item_id)
        messages.success(
            request, f'Removed {watch.name} from your shopping cart')

    request.session['shoppingcart'] = shoppingcart
    return redirect(reverse('shoppingcart'))


def remove_from_shoppingcart(request, item_id):
    """ Remove a specified product from the shopping bag """

    try:
        watch = get_object_or_404(Watch, pk=item_id)
        shoppingcart = request.session.get('shoppingcart', {})
        shoppingcart.pop(item_id)
        messages.success(
            request, f'Removed {watch.name} from your shopping cart')

        request.session['shoppingcart'] = shoppingcart
        return HttpResponse(status=200)
    
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)