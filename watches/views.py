from django.shortcuts import render
from .models import Watch

# Create your views here.


def all_watches(request):
    """  A view to all watches including any sorting and search queries  """
   
    watches = Watch.objects.all()

    context = {
        'watches': watches,
    }
   
    return render(request, 'watches/all_watches.html', context)