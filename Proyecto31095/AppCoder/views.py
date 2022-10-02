from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import django
import datetime
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from AppCoder.models import *
from AppCoder.forms import *

def inicio(request):
    blogs = Blog.objects.all()

    contexto = {'blogs': blogs,
        'form': BusquedaBlogFormulario()
        }

    return render(request, 'index.html', contexto)

""" def blog_crear(request):

    return
 """
def blog_editar(request, numero):
    blog_editar = Blog.objects.get(numero=numero)

    if request.method == 'POST':
        mi_formulario = BlogFormulario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            blog_editar.nombre = data.get('nombre')
            blog_editar.numero = data.get('numero')
            try:
                blog_editar.save()
            except django.db.utils.IntegrityError:
                messages.ERROR(request, "La modificacion fallo por que el numero esta repedita")

            return redirect('AppCoderBlog')
    
    blogs = Blog.objects.all()

    contexto = {
        'form': BlogFormulario(
            initial={
                "nombre": blog_editar.nombre,
                "numero": blog_editar.numero,
            }
        ),
        'blogs': blogs
    }

    return render(request, 'AppCoder/blog_formulario.html', contexto)

def blog_eliminar(request, numero):
    blog_eliminar = Blog.objects.get(numero= numero)
    blog_eliminar.delete()

    messages.info(request ,f"El blog {blog_eliminar} fue eliminado")

    return redirect('AppCoderBlog')

def blog_busqueda(request):

    numero = request.POST.get('numero') or 0

    blogs = Blog.objects.filter(numero__icontains=numero)
    """ '__exact' para usar el filtro de manera exacta """
    contexto = {
        'forms': BusquedaBlogFormulario(),
        'blogs': blogs
    }
    return render(request, 'AppCoder/busqueda_blog.html', contexto)

def about (request):
    return render(request, 'AppCoder/about.html')

@ login_required

def blog_formulario(request):

    if request.method == 'POST':
        mi_formulario = BlogFormulario(request.POST)
        
        blogs = Blog.objects.all()
        numero = len(blogs) + 1

        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data

            print(data)

            blog1 = Blog(nombre=data.get('nombre'), subtitulo=data.get('subtitulo'), numero=numero, contenido=data.get('contenido'),autor=data.get('autor'), fecha=str(datetime.datetime.now))
            blog1.save()
            return redirect('AppCoderInicio')
        
    blogs = Blog.objects.all()

    contexto = {
        'form': BlogFormulario(),
        'blogs': blogs
    }
    return render(request, 'AppCoder/blog_formulario.html', contexto)

class CreateBlog(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = CreateBlogForm
    template_name = "AppCoder/blog_formulario.html"
    login_url = 'login'
    success_url = "/"
    success_message = "Your blog has been created"
""" 
def profesores(request):

    if request.method == 'POST':
        mi_formulario = ProfesoresFormulario(request.POST)

        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data

            profesor1 = Profesor(nombre=data.get('nombre'), apellido=data.get('apellido'), email=data.get('email'), profesion=data.get('profesion'))
            profesor1.save()
            
            return redirect('AppCoderInicio')

    contexto = {'form': ProfesoresFormulario()}

    return render(request, 'AppCoder/profesores_formulario.html', contexto) """
""" 
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
    return render(request, 'AppCoder/estudiantes_formulario.html', contexto) """