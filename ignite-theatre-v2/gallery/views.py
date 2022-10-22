from django.shortcuts import render
from .models import Image


def all_images(request):
    '''A view to show all images'''
    '''context = to allow things to be sent to template'''
    
    images = Image.objects.all()

    context = {
        'images': images
    }

    return render(request, 'gallery/gallery.html', context)