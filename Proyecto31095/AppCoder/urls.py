from django.urls import path

from AppCoder.views import familia, inicio

urlpatterns = [
    path('', inicio, name=('AppCoderInicio')),
    path('familia/', familia, name='AppCoderFamilia'),
]