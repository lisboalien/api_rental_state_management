from django.contrib import admin
from rental_state.models import RentalState


class rental_states(admin.ModelAdmin):
    list_display = ('id', 'rental_state_code', 'description', 'rental_state_type', 'property_type', 'address',
                 'footage', 'unit', 'number_of_rooms', 'number_of_bathrooms', 'garage_for_how_many_cars')
    list_display_links = ('id', 'rental_state_code')
    search_fields = ('rental_state_type', 'property_type',)
    list_per_page = 20

admin.site.register(RentalState, rental_states)
