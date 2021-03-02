from django.contrib import admin
from .models import Watch, Brand, Category

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

    ordering = ('sku',)
    

class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'image',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',    
    )

admin.site.register(Watch, WatchAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)