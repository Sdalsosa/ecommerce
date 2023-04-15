from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from prints.models import Print


def cart_content(request):

    cart_prints = []
    total = 0
    print_count = 0
    free_delivery_count = 0
    cart = request.session.get('cart', {})

    for id, quant in cart.items():
        print = get_object_or_404(Print, pk=id)
        total += quant * print.price
        print_count += quant
        cart_prints.append({
            'id': id,
            'quant': quant,
            'print': print,
        })
    
    if print_count > 5:
        delivery = 0
    else:
        delivery = 15

    if print_count == 0:
        grand_total = 0
    else:
        grand_total = delivery + total

    if print_count < 5:
        free_delivery_count = 5 - print_count
    else:
        free_delivery_count = 0

    context = {
        'cart_prints': cart_prints,
        'total': total,
        'print_count': print_count,
        'delivery': delivery,
        'free_delivery_count': free_delivery_count,
        'grand_total': grand_total,
    }

    return context
