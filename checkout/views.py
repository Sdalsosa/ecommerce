from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('prints'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key' : 'pk_test_51MxW5sEP3491zwROF1DHtkrbqPQIsrQlu9aHmpbIQeTvFdVC39pI6Iy0BxfQ0uBBiYAJ7Ayz2sQrpQXhHeSHpaH200uENvRC1Q',
        'client_secret' : 'test client secret',
    }

    return render(request, template, context)
