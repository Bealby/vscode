from django.shortcuts import render


def index(request):
# A view to return bag contents page

    return render(request, 'bag/bag.html')