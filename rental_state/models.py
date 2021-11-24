from django.db import models


class RentalState(models.Model):
    RENTAL_STATE_TYPE = (
        ('C', 'COMERCIAL'),
        ('R', 'RESIDENCIAL')
    )

    TYPE = (
        ('AP', 'APARTAMENTO'),
        ('CA', 'CASA'),
        ('CC', 'CASA DE CONDOMÍNIO'),
        ('CO', 'COBERTURA'),
        ('FL', 'FLAT'),
        ('SO', 'SOBRADO')
    )

    rental_state_code = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=False, null=False)
    rental_state_type = models.CharField(
        max_length=1, choices=RENTAL_STATE_TYPE, blank=False, null=False, default='R')
    property_type = models.CharField(
        max_length=2, choices=TYPE, blank=False, null=False, default='AP')
    address = models.CharField(max_length=1000)
    footage = models.CharField(max_length=100)
    unit = models.CharField(max_length=2, blank=False,
                            null=False, default='m2')
    number_of_rooms = models.CharField(max_length=10)
    number_of_bathrooms = models.CharField(max_length=10)
    garage_for_how_many_cars = models.CharField(max_length=10)

    def __str__(self):
        return self.description
