from django.shortcuts import render

# Create your views here.

def view_shopping_cart(request):
    """  A view to render the shopping cart  """
    
    return render(request, 'shopping_cart/shopping_cart.html')