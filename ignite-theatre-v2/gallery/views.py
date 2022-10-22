from django.shortcuts import render
from .models import Image


def all_gallery(request):
    '''A view to show all images'''
    '''context = to allow things to be sent to template'''
    
    gallery = Image.object.all()

    context = {
        'gallery': gallery,
    }

    return render(request, 'gallery/gallery.html', context)