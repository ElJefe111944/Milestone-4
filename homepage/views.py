from django.shortcuts import render

# Create your views here.


def index(request):
    """  A view to return the homepage  """

    return render(request, 'homepage/index.html')
