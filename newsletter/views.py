from django.shortcuts import render, redirect
from .forms import SubscriberForm
from django.contrib import messages


def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Thank you for Subscribing - Use code "WELCOME50" for €50 off your first order!')
            return redirect('home')
    else:
        form = SubscriberForm()

    context = {
        'form': form
    }
    template = 'newsletter/subscribe.html'
    return render(request, template, context)
