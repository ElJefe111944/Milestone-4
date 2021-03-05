from django.shortcuts import render

# Create your views here.


def view_shoppingcart(request):
    """  A view to render the shopping cart  """
    
    return render(request, 'shoppingcart/shoppingcart.html')