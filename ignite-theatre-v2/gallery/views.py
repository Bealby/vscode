from django.shortcuts import render
from .models import Gallery
from .models import Show


def all_galleries(request):
    '''A view to show all images'''
    '''context = to allow things to be sent to template'''
    
    galleries = Gallery.objects.all()
    show = None

    if request.GET:
        if 'show' in request.GET:
            shows = request.GET['show'].split(',')
            galleries = galleries.filter(name__in=shows)
            shows = Show.objects.filter(name__in=shows)

    context = {
        'galleries': galleries,
        'current_shows': shows,
    }

    return render(request, 'gallery/gallery.html', context)