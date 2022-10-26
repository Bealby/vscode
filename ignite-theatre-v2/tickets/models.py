from django.db import models
'''Pillow must be installed'''


class Show(models.Model):
    
    '''Programmatic Name'''
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    poster = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Ticket(models.Model):

    show = models.ForeignKey('show', null=True, blank=True, on_delete=models.SET_NULL)
    date = models.CharField(max_length=254)
    place = models.CharField(max_length=254)
    Location = models.CharField(max_length=254)

    def __str__(self):
        return self.name
