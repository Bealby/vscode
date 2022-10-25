from django.contrib import admin
from .models import Show
from .models import Actor
from .models import Crew


class ShowAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ActorAdmin(admin.ModelAdmin):
    list_display = (
        'show',
        'name',
        'image',
        'description',
        'role',
        'wensite',
    )

class CrewAdmin(admin.ModelAdmin):
    list_display = (
        'show',
        'name',
        'role',
    )


admin.site.register(Show, ShowAdmin)
admin.site.register(Actor, ActorAdmin)
