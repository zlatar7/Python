from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import django
import datetime
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from AppCoder.models import *
from AppCoder.forms import *

def inicio(request):
    blogs = Blog.objects.all()

    contexto = {'posts': blogs,
        'form': BusquedaBlogFormulario()
        }

    return render(request, 'index.html', contexto)

def detalles(request, titulo='Python'):
    blog_seleccionado = Blog.objects.get(title = titulo)
    
    contexto = {'blog': blog_seleccionado}

    return render(request, 'AppCoder/blog_detalles.html', contexto)

def blog_busqueda(request):

    titulo = request.POST.get('title') or ""

    blogs = Blog.objects.filter(title__icontains=titulo)

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

            blog1 = Blog(nombre=data.get('nombre'), subtitulo=data.get('subtitulo'), numero=numero, contenido=data.get('contenido'),autor=data.get('autor'), fecha=str(datetime.datetime.now))
            blog1.save()
            return redirect('AppCoderInicio')
        
    blogs = Blog.objects.all()

    contexto = {
        'form': BlogFormulario(),
        'blogs': blogs
    }
    return render(request, 'AppCoder/blog_formulario.html', contexto)

def blog_editar(request, titulo):

    blog_editar = Blog.objects.filter(title__icontains= titulo)

    if request.method == 'POST':
        mi_formulario = CreateBlogForm(request.POST)
    
        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data
            try:
                for i in blog_editar:
                    i.title = data.get('title')
                    i.author = data.get('author')
                    i.subtitle = data.get('subtitle')
                    i.description = data.get('description')
                    i.post_date = datetime.date.today()
                    i.slug = data.get('slug')

                    i.save()
                
            except django.db.utils.IntegrityError:
                messages.ERROR(request, "La modificación ha fallado. Intente nuevamente")

            return redirect('AppCoderEdicionBlog')
    
    blogs = Blog.objects.all()

    contexto = {
        'form': CreateBlogForm(
            initial={
                "title": titulo,        
            }),
        'blogs': blogs
    }
   
    return render(request, 'AppCoder/blog_editar.html', contexto)

def blog_edicion (request):
    blogs = Blog.objects.all()

    contexto = {'blogs': blogs }
    return render(request, 'AppCoder/blog.html', contexto)

def blog_eliminar(request, titulo):
    blog_eliminar = Blog.objects.filter(title__exact= titulo)
    blog_eliminar.delete()

    messages.info(request ,f"El blog {titulo} fue eliminado")

    return redirect('AppCoderEdicionBlog')

class CreateBlog(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = CreateBlogForm
    template_name = "AppCoder/blog_formulario.html"
    login_url = 'login'
    success_url = "/"
    success_message = "El blog ha sido creado satisfactoriamente"
