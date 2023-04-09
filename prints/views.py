from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Print


def prints(request):
    """ A view to show all prints """
    prints = Print.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
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
                messages.error(reqiest, "Please enter a proper search word")
                return redirect(reverse('prints'))

            queries = Q(name__icontains=query) | Q(
                        description__icontains=query)
            prints = prints.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'prints': prints,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'prints/prints.html', context)


def single_print(request, pk):
    """ A view to show single print """
    print = get_object_or_404(Print, pk=pk)

    return render(request, 'prints/single_print.html', {'print': print, })
