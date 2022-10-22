from django.db import models
'''Pillow must be installed'''


class Show(models.Model):
    '''Programmatic Name'''
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Image(models.Model):
    '''null=True, blank=True are optional fields'''
    show = models.ForeignKey('show', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


