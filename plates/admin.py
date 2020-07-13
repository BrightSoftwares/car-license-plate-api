from django.contrib import admin

from .models import Plate, Owner


class PlateAdmin(admin.ModelAdmin):
    list_display = ('id', 'license_number', 'accuracy', 'owner', 'detector',)
    search_fields = ['license_number']


class PlateInline(admin.TabularInline):
    model = Plate
    extra = 1


class OwnerAdmin(admin.ModelAdmin):
    inlines = [PlateInline]
    list_display = ('id', 'name', 'surname', 'total_plates')
    search_fields = ['surname']


admin.site.register(Plate, PlateAdmin)
admin.site.register(Owner, OwnerAdmin)
