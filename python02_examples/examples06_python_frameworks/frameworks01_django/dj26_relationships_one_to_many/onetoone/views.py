from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant

def create(request):
    # Crear todos los elementos
    place = Place(name="Lugar 1", address="Avenida siempre viva")
    place.save()

    restaurant = Restaurant(place=place, number_of_employees=8)
    restaurant.save()
    return HttpResponse(restaurant.place.name)