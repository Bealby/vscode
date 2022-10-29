from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404       
from tickets.models import Ticket


def view_bag(request):
# A view to return bag contents page

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    '''Submit form to this view including ticket id and quanity'''
    ''' Add a quantity of the specified tickets to the shopping bag'''

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    '''Once in view get bag variable if exisits in session or create if doesn't'''

    '''Add to bag'''
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
