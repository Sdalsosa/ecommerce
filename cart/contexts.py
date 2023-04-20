from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from prints.models import Print


def cart_content(request):

    cart_prints = []
    total = 0
    print_count = 0
    free_delivery = 0
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
    
    if total < 1000:
        free_delivery = 1000 - total
    else:
        free_delivery = 0

    if total > 1000:
        delivery = 0
    else:
        delivery = 15

    if print_count == 0:
        grand_total = 0
    else:
        grand_total = delivery + total

    context = {
        'cart_prints': cart_prints,
        'total': total,
        'delivery': delivery,
        'free_delivery': free_delivery,
        'grand_total': grand_total,
    }

    return context
