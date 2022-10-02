from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from AppCoder.views import *
from AppCoder import views
urlpatterns = [
    path('', inicio, name=('AppCoderInicio')),
    path('blog_formulario/', views.CreateBlog.as_view(), name="create-blog"),
    path('blog_busqueda/', blog_busqueda, name='AppCoderBusquedaBlog'),
    path('about/', about, name='AppCoderAbout'),
    path('eliminar_blog/<int:numero>', blog_eliminar, name='AppCoderEliminarBlog'),
    path('editar_blog/<int:numero>', blog_editar, name='AppCoderEditarBlog'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)