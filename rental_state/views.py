from django.shortcuts import render
from django.http import JsonResponse

def rental_state(request):
    if request.method == 'GET':
        rental_state = {'id':1, 'type': 'Apartment', 'footage': '100', 'unit': 'square meters'}
        return JsonResponse(rental_state)