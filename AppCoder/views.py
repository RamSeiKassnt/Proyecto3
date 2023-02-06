from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Profesor

# Create your views here.

def inicio(request):
    return HttpResponse ("Hola, bienvenidos a mi pagina")

def agregar_profe(request):
    profe1 = Profesor(nombre="Rama", apellido="SeiKassnt",email="rama@seikassnt.com",profesion="economista")
    profe1.save()

    return HttpResponse(f"Hemos agregado al nuevo profesor {profe1.nombre} a la base de datos")