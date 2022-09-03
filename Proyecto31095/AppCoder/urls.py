from django.urls import path
from django.views.generic import ListView

from AppCoder.views import curso, inicio, curso_formulario, curso_busqueda, profesores, eliminar_curso, editar_curso

urlpatterns = [
    path('', inicio, name=('AppCoderInicio')),
    path('curso/', curso, name='AppCoderCurso'),
    path('curso_formulario/', curso_formulario, name='AppCoderCursoFormulario'),
    path('busqueda_camada/', curso_busqueda, name='AppCoderBusquedaCamada'),
    path('profesores_formulario/', profesores, name='AppCoderProfesores'),
    path('eliminar_curso/<int:camada>', eliminar_curso, name='AppCoderEliminarCurso'),
    path('editar_curso/<int:camada>', editar_curso, name='AppCoderEditarCurso'),
]