from django.contrib import admin
from .models import Watch, Brand

# Register your models here.


class WatchAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'brand',      
        'price',
        'rating',
        'image',
    )

    ordering = ('sku')
    

class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'image',
    )


admin.site.register(Watch, WatchAdmin)
admin.site.register(Brand, BrandAdmin)