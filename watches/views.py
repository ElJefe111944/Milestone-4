from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Watch, Category
from .forms import ProductForm

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


@login_required
def add_watch(request):
    """ Add a watch to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            watch = form.save()
            messages.success(request, 'Watch successfully added to store!')
            return redirect(reverse('watch_detail', args=[watch.id]))
        else:
            messages.error(
                request, 'Failed to add watch as the form is invalid.')
    else:
        form = ProductForm()
    
    template = 'watches/add_watch.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_watch(request, watch_id):
    """ Edit a watch currently in store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can do that.')
        return redirect(reverse('home'))

    watch = get_object_or_404(Watch, pk=watch_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=watch)
        if form.is_valid():
            form.save()
            messages.success(request, f'{watch.name} successfully updated.')
            return redirect(reverse('watch_detail', args=[watch.id]))
        else:
            messages.error(request, 'Unable to update item. \
                     Please check that the form is valid')
    else:
        form = ProductForm(instance=watch)
        messages.info(request, f'You are editing {watch.name}')

    template = 'watches/edit_watch.html'
    context = {
        'form': form,
        'watch': watch,
    }

    return render(request, template, context)


@login_required
def delete_watch(request, watch_id):
    """ Delete a watch currently in store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can do that.')
        return redirect(reverse('home'))

    watch = get_object_or_404(Watch, pk=watch_id)
    watch.delete()
    messages.success(request, 'Watch successfully deleted.')

    return redirect(reverse('watches'))
