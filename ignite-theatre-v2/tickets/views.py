from django.shortcuts import render


def tickets(request):
    # A view to return the tickets page
    return render(request, "tickets/tickets.html")