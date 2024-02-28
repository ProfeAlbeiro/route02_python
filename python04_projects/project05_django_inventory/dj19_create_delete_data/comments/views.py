from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

def test(request):
    return HttpResponse("Funciona correctamente")

def create(request):
    comment = Comment(name="Juanjo", score=5, comment="Este es un comentario")
    comment.save()
    return HttpResponse("Ruta para la creación de modelos")