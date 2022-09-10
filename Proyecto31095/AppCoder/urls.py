from django.urls import path

from AppCoder.views import *

urlpatterns = [
    path('', inicio, name=('AppCoderInicio')),
    path('curso/', curso, name='AppCoderCurso'),
    path('curso_formulario/', curso_formulario, name='AppCoderCursoFormulario'),
    path('busqueda_camada/', curso_busqueda, name='AppCoderBusquedaCamada'),
    path('profesores_formulario/', profesores, name='AppCoderProfesoresFormulario'),
    path('eliminar_curso/<int:camada>', eliminar_curso, name='AppCoderEliminarCurso'),
    path('editar_curso/<int:camada>', editar_curso, name='AppCoderEditarCurso'),
    path('estudiantes_formulario', estudiantes_formulario, name='AppCoderEstudiantesFormulario'),
]