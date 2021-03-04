from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Watch, Category
from django.db.models.functions import Lower

# Create your views here.


def all_watches(request):
    """  A view to show an individual watch  """
   
    watches = Watch.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                watches = watches.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            watches = watches.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            watches = watches.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('all_watches'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            watches = watches.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'watches': watches,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting, 
    }
   
    return render(request, 'watches/all_watches.html', context)


def watch_detail(request, watch_id):
    """  A view to all watches including any sorting and search queries  """
   
    watch = get_object_or_404(Watch, pk=watch_id)

    context = {
        'watch': watch,
    }
   
    return render(request, 'watches/watch_detail.html', context)