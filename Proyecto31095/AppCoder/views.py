from django.shortcuts import render, redirect
from django.contrib import messages
import django

from AppCoder.models import Curso, Profesor, Estudiante
from AppCoder.forms import CursoFormulario, BusquedaCamadaFormulario, ProfesoresFormulario, EstudiantesFormulario

def inicio(request):
    contexto = {
        'form': BusquedaCamadaFormulario()
        }

    return render(request, 'index.html', contexto)

def editar_curso(request, camada):
    curso_editar = Curso.objects.get(camada=camada)

    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            curso_editar.nombre = data.get('nombre')
            curso_editar.camada = data.get('camada')
            try:
                curso_editar.save()
            except django.db.utils.IntegrityError:
                messages.error(request, "la modificacion fallo por que la camada esta repedita")

            return redirect('AppCoderCurso')
    
    cursos = Curso.objects.all()

    contexto = {
        'form': CursoFormulario(
            initial={
                "nombre": curso_editar.nombre,
                "camada": curso_editar.camada,
            }
        ),
        'cursos': cursos
    }

    return render(request, 'AppCoder/curso_formulario.html', contexto)

def eliminar_curso(request, camada):
    curso_eliminar = Curso.objects.get(camada= camada)
    curso_eliminar.delete()

    messages.info(request ,f"El curso {curso_eliminar} fue eliminado")

    return redirect('AppCoderCurso')

def curso (request):

    cursos = Curso.objects.all()

    contexto= {'cursos': cursos}

    return render(request, 'AppCoder/curso.html', contexto)

def curso_formulario(request):

    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)

        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data

            curso1 = Curso(nombre=data.get('nombre'), camada=data.get('camada'))
            curso1.save()
            
            return redirect('AppCoderCurso')
        
    cursos = Curso.objects.all()

    contexto = {
        'form': CursoFormulario(),
        'cursos': cursos
    }
    return render(request, 'AppCoder/curso_formulario.html', contexto)

def curso_busqueda(request):

    camada = request.POST.get('camada') or 0

    cursos = Curso.objects.filter(camada__icontains=camada)
    """ '__exact' para usar el filtro de manera exacta """
    contexto = {
        'forms': BusquedaCamadaFormulario(),
        'cursos': cursos
    }
    return render(request, 'AppCoder/busqueda_camada.html', contexto)

def profesores(request):

    if request.method == 'POST':
        mi_formulario = ProfesoresFormulario()(request.POST)

        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data

            curso1 = Profesor(nombre=data.get('nombre'), apellido=data.get('camada'), email=data.get('email'), profesion=data.get('profesion'))
            curso1.save()
            
            return redirect('AppCoder/')

    contexto = {'form': ProfesoresFormulario()}

    return render(request, 'AppCoder/profesores_formulario.html', contexto)

def estudiantes_formulario (request):

    if request.method == 'POST':
        mi_formulario = EstudiantesFormulario(request.POST)

        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data

            curso1 = Estudiante(nombre=data.get('nombre'), apellido=data.get('apellido'), email=data.get('email'))
            curso1.save()
            
            return redirect('AppCoderInicio')
          
    contexto = {
        'form': EstudiantesFormulario()
    }
    return render(request, 'AppCoder/estudiantes_formulario.html', contexto)