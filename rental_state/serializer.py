from rest_framework import serializers
from rental_state.models import RentalState

class RentalStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalState
        fields = '__all__'