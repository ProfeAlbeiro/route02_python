from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return HttpResponse("Funciona correctamente")

def create(request):
    return HttpResponse("Ruta para la creación de modelos")