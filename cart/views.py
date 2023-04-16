from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from prints.models import Print


def view_cart(request):
    """ Shopping Cart Page View """

    return render(request, 'cart/cart.html')


def add_to_cart(request, pk):
    """ add print quantity to cart """

    item = Print.objects.get(pk=pk)
    redirect_url = request.POST.get('redirect_url')
    quant = int(request.POST.get('quant'))
    cart = request.session.get('cart', {})

    if pk in list(cart.keys()):
        cart[pk] += quant
    else:
        cart[pk] = quant
        messages.success(request, f'Added {item.name} to your cart')

    request.session['cart'] = cart

    return redirect(redirect_url)


def update_cart(request, pk):
    """ update prints in cart """
    quant = int(request.POST.get('quant'))
    cart = request.session.get('cart', {})

    if quant > 0:
        cart[pk] = quant
    else:
        cart.pop(pk)

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))


def remove_from_cart(request, pk):
    """ update prints in cart """

    try:
        cart = request.session.get('cart', {})

        cart.pop(pk)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)