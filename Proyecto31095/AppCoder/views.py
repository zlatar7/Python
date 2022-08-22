from django.shortcuts import render
from datetime import datetime

from AppCoder.models import Familia


def familia (request):
    persona1 = Familia(nombre="Guido", apellido="Zlatar", edad=27, fecha=datetime.now())
    persona2 = Familia(nombre="Guille", apellido="Zlatar", edad=33, fecha=datetime.now())
    persona3 = Familia(nombre="Norma", apellido="Acevedo", edad=47, fecha=datetime.now())
    persona1.save()
    persona2.save()
    persona3.save()

    contexto= {'persona1': persona1,'persona2': persona2,'persona3': persona3,}

    return render(request, 'familia.html', contexto)