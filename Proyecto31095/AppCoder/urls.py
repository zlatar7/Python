from django.urls import path

from AppCoder.views import familia, inicio

urlpatterns = [
    path('', inicio),
    path('familia/', familia, name='AppCoderFamilia'),
]