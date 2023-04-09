from django.shortcuts import render, get_object_or_404
from .models import Print


def prints(request):
    """ A view to show all prints """
    prints = Print.objects.all()

    return render(request, 'prints/prints.html', {'prints': prints, })


def single_print(request, pk):
    """ A view to show single print """
    print = get_object_or_404(Print, pk=pk)

    return render(request, 'prints/single_print.html', {'print': print, })
