from rest_framework import viewsets
from rental_state.models import RentalStateProperty
from rental_state.serializer import RentalStateSerializer


class RentalStateViewSet(viewsets.ModelViewSet):
    """Showing all the properties in the database"""
    queryset = RentalStateProperty.objects.all()
    serializer_class = RentalStateSerializer
