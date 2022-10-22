from django.shortcuts import render
from .models import Image


def all_gallery(request):
    '''A view to show all images'''
    '''context = to allow things to be sent to template'''
    
    gallery = Image.objects.all()
    show = None

    if request.GET:
        if 'show' in request.GET:
            shows = request.GET['show'].split(',')
            gallery = gallery.filter(show__name__in=shows)

    context = {
        'gallery': gallery
    }

    return render(request, 'gallery/gallery.html', context)