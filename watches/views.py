from django.shortcuts import render, get_object_or_404
from .models import Watch

# Create your views here.


def all_watches(request):
    """  A view to show an individual watch  """
   
    watches = Watch.objects.all()

    context = {
        'watches': watches,
    }
   
    return render(request, 'watches/all_watches.html', context)


def watch_detail(request, watch_id):
    """  A view to all watches including any sorting and search queries  """
   
    watch = get_object_or_404(Watch, pk=watch_id)

    context = {
        'watch': watch,
    }
   
    return render(request, 'watches/watch_detail.html', context)