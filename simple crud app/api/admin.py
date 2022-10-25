from django.contrib import admin

from .models import Location, Item

# Register your models here.
# another way of registering to admin site
@admin.register(Item)
class ItemsList(admin.ModelAdmin):
    list_display = ['id', 'itemName', 'itemLocation']
@admin.register(Location)
class ItemsList(admin.ModelAdmin):
    list_display = ['id', 'locationName']

# admin.site.register(Location)
# admin.site.register(Item)
