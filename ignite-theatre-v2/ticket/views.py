from django.shortcuts import render


def ticket(request):
    # A view to return the ticket page
    return render(request, "ticket/ticket.html")