from django.shortcuts import render
from django.http import HttpResponse

def form(request):
    return render(request, 'form.html', {})

def goal(request):
    if request.method != 'GET':
        return HttpResponse('El método POST no está soportado en esta ruta')
    
    
    name = request.GET['name']
    return render(request, 'success.html', {'name': name})
        