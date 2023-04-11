from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Print, Category
from django.db.models import Count
from django.db.models.functions import Lower


def prints(request):
    """ A view to show all prints """
    prints = Print.objects.all()
    categories = Category.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:

        if 'category' in request.GET:
            selection = request.GET['category'].split(',')
            if 'all' not in selection:
                prints = prints.filter(category__name__in=selection)
                
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'likes':
                prints = prints.annotate(
                        likes_count=Count('likes')).order_by('-likes_count')
            elif sortkey == 'name':
                sortkey = 'lower_name'
                prints = prints.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                prints = prints.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a proper search word")
                return redirect(reverse('prints'))

            queries = Q(name__icontains=query) | Q(
                        description__icontains=query)
            prints = prints.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'prints': prints,
        'search_term': query,
        'current_sorting': current_sorting,
        'categories': categories,
    }

    return render(request, 'prints/prints.html', context)


def single_print(request, pk):
    """ A view to show single print """
    print = get_object_or_404(Print, pk=pk)

    return render(request, 'prints/single_print.html', {'print': print, })
