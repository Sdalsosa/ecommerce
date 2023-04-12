from django.shortcuts import render

""" Shopping Cart Page View """


def view_cart(request):
    return render(request, 'cart/cart.html')
