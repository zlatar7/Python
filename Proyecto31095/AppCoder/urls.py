from django.urls import path

from AppCoder.views import familia, inicio, curso_formulario, curso_busqueda

urlpatterns = [
    path('', inicio, name=('AppCoderInicio')),
    path('familia/', familia, name='AppCoderFamilia'),
    path('curso_formulario/', curso_formulario, name='AppCoderCursoFormulario'),
    path('busqueda_camada/', curso_busqueda, name='AppCoderBusquedaCamada'),
]