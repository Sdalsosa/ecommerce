from django.shortcuts import render, redirect


def view_cart(request):
    """ Shopping Cart Page View """

    return render(request, 'cart/cart.html')


def add_to_cart(request, pk):
    """ add print quantity to cart """

    quant = int(request.POST.get('quant'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if pk in list(cart.keys()):
        cart[pk] += quant
    else:
        cart[pk] = quant

    request.session['cart'] = cart

    return redirect(redirect_url)
