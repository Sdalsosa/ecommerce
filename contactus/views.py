from django.shortcuts import render, redirect
from .forms import ContactUsForm
from django.contrib import messages


def contactus(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Thank you for your message! We will get back to you shortly')
            return render(request, 'home/index.html')
    else:
        form = ContactUsForm()
        return render(request, 'contactus/contactus.html', {'form': form})


def about(request):
    return render(request, 'contactus/about.html')
