from django.conf import settings

def bag_contents(request):

    bag_items = []
    '''Empty list for bag items to live in'''
    total = 0
    product_count = 0

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    '''Make dictionary available to all templates across the enitire application'''
    return context

