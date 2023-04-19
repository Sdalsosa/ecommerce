from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from likes.models import Like
from prints.models import Print


def like(request, pk):
    print = get_object_or_404(Print, id=request.POST.get('print_id'))
    liked = False
    if print.likes.filter(id=request.user.id).exists():
        print.likes.remove(request.user)
        liked = False
    else:
        print.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('single_print', args=[str(pk)]))
