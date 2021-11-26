from rest_framework import serializers
from rental_state.models import RentalStateProperty

class RentalStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalStateProperty
        fields = '__all__'