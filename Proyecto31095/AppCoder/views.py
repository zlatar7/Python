from django.shortcuts import render, redirect
from datetime import datetime

from AppCoder.models import Familia, Curso
from AppCoder.forms import CursoFormulario, BusquedaCamadaFormulario

def inicio(request):
    return render(request, 'index.html')

def familia (request):

    persona1 = Familia(nombre="Guido", apellido="Zlatar", edad=27, fecha=datetime.now())
    persona2 = Familia(nombre="Guille", apellido="Zlatar", edad=33, fecha=datetime.now())
    persona3 = Familia(nombre="Norma", apellido="Acevedo", edad=47, fecha=datetime.now())
    persona1.save()
    persona2.save()
    persona3.save()

    contexto= {'persona1': persona1,'persona2': persona2,'persona3': persona3,}

    return render(request, 'AppCoder/familia.html', contexto)

def curso_formulario(request):

    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)

        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data

            curso1 = Curso(nombre=data.get('nombre'), camada=data.get('camada'))
            curso1.save()
            
            return redirect('AppCoderCursoFormulario')
        
    cursos = Curso.objects.all()

    contexto = {
        'form': CursoFormulario(),
        'cursos': cursos
    }
    return render(request, 'AppCoder/curso_formulario.html', contexto)

def curso_busqueda(request):

    camada = request.POST.get('camada')

    cursos = Curso.objects.filter(camada__icontains=camada)
    """ __exact para usar el filtro de manera exacta """
    contexto = {
        'form': BusquedaCamadaFormulario(),
        'cursos': cursos
    }
    return render(request, 'AppCoder/busqueda_camada.html', contexto)
