
from decimal import Decimal
from django.conf import settings


def cart_content(request):

    cart_items = []
    total = 0
    item_count = 0

    if item_count > 5:
        delivery = 20
    else:
        delivery = 15

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
