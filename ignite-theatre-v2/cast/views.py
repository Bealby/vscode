from django.shortcuts import render
from .models import Show
from .models import Cast
from .models import Crew


def all_actors(request):
    '''A view to show all images'''
    '''context = to allow things to be sent to template'''
    
    casts = Cast.objects.all()
    crews = Crew.objects.all()
    '''Filter actors by show'''
    shows = None

    '''Request if show exists'''
    if request.GET:
        if 'show' in request.GET:
            '''If show exists split into a list at the commas'''
            shows = request.GET['show'].split(',')
            '''Use the list to filter gallery only related to the show '''
            '''Name in Show.model '''
            casts = casts.filter(show__name__in=shows)
            crews = crews.filter(show__name__in=shows)
            '''Display to user which show they have currently selected'''
            shows = Show.objects.filter(name__in=shows)

    context = {
        'cast': casts,
        'crews': crews,
        'current_shows': shows,
    }

    return render(request, 'cast/cast.html', context)