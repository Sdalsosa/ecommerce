from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from prints.models import Print


def cart_content(request):

    cart_prints = []
    total = 0
    print_count = 0
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
        delivery = 20
    else:
        delivery = 15

    if print_count == 0:
        grand_total = 0
    else:
        grand_total = delivery + total

    context = {
        'cart_prints': cart_prints,
        'total': total,
        'print_count': print_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
