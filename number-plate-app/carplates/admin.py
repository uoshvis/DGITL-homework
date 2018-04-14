from django.contrib import admin

from carplates.models import CarPlate


class CarplateAdmin(admin.ModelAdmin):
    # readonly_fields=('plate_number',)
    search_fields = ['plate_number', 'last_name']
    list_display = ('plate_number', 'last_name', 'first_name')
    fieldsets = [
        (None, {'fields': ['plate_number']}),
        ('Owner information', {'fields': ['last_name', 'first_name']})
    ]

    def get_readonly_fields(self, request, obj=None):
        # obj is not None, so this is an edit
        if obj:
            # Return a list or tuple of readonly fields' names
            return ['plate_number']
        # This is an addition
        else:
            return []


admin.site.register(CarPlate, CarplateAdmin)
