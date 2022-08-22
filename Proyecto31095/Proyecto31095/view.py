from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime 

def saludo(request):
    return HttpResponse("Estoy saludando desde DJANGO")

def segunda_vista (request):
    ahora = datetime.now()
    mensaje = f'Esta es mi segunda vista y fue ejecutada el {ahora}'
    return HttpResponse(mensaje)

def tercera_vista(request, nombre):
    mensaje = f"Hola {nombre}, bienvenido a nuestra plataforma"
    return HttpResponse(mensaje)

def template_1(request):
    
    contexto = {"nombre": "Guido", "edad": 27}

    return render(request, "template.html", contexto)

def template_2(request, nombre, edad):
    
    contexto = {
        "nombre": nombre,
        "edad": edad,
        "fecha": datetime.now(),
        "lista": [1,2,3,4,5],
        "diccionario": {"animal": "perro"}
    }

    return render(request, "template.html", contexto)