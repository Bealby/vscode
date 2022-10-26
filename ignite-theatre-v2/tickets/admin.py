from django.contrib import admin
from .models import Show
from .models import Ticket


class ShowAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'poster',
    )

class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'show',
        'event',
        'place',
        'location',
        'position',
    )

    ordering = ('position',)

admin.site.register(Show, ShowAdmin)
admin.site.register(Ticket, TicketAdmin)