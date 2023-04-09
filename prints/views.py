from django.shortcuts import render
from .models import Print


def prints(request):
    """ A view to show all prints """
    prints = Print.objects.all()

    return render(request, 'prints/prints.html', {'prints': prints, })
