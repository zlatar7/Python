from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from AppCoder.views import *
from AppCoder import views

urlpatterns = [
    path('', inicio, name=('AppCoderInicio')),
    path('detalles/<str:titulo>', detalles, name=('AppCoderDetalles')),
    path('blog_formulario/', views.CreateBlog.as_view(), name="create-blog"),
    path('blog_busqueda/', blog_busqueda, name='AppCoderBusquedaBlog'),
    path('about/', about, name='AppCoderAbout'),
    path('eliminar_blog/<str:titulo>', blog_eliminar, name='AppCoderEliminarBlog'),
    path('blog_editar/<str:titulo>', blog_editar, name='AppCoderEditarBlog'),
    path('blog_edicion/', blog_edicion, name='AppCoderEdicionBlog'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)