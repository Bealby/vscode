from django.contrib import admin
from .models import Image
from .models import Show


class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'show',
        'name',
        'description',
        'picture',
    )

class ShowAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Image, ImageAdmin)
admin.site.register(Show, ShowAdmin)
