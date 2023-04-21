from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import ContactUsForm
from django.contrib import messages
from .models import ContactUs


def contactus(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Thank you for your message! We will get back to you shortly')
            return render(request, 'home/index.html')
    else:
        form = ContactUsForm()

        context = {
            'form': form
        }

        return render(request, 'contactus/contactus.html', context)


def about(request):
    return render(request, 'contactus/about.html')


def contactus_messages(request):
    message_list = ContactUs.objects.all()

    context = {
        'message_list': message_list
    }

    return render(request, 'contactus/messages.html', context)


def single_message(request, pk):
    """ A view to show single message """
    single_message = get_object_or_404(ContactUs, pk=pk)

    context = {
        'single_message': single_message
    }

    return render(request, 'contactus/single_message.html', context)


def delete_message(request, pk):
    """ A view to show delete a message """
    single_message = get_object_or_404(ContactUs, pk=pk)
    single_message.delete()
    messages.success(request, 'Successfully deleted message!')

    return redirect('messages')
