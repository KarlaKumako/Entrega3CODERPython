from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso

def curso(req, nombre, camada):

   nuevo_curso= Curso(nombre=nombre, camada=camada)
   nuevo_curso.save()
   
   return HttpResponse(f""" <p>Curso: {nuevo_curso.nombre} - Camada:{nuevo_curso.camada} creado </p>""")

def lista_cursos(req):

   lista= Curso.objects.all()

   return render(req,"lista_cursos.html", {"lista_cursos":lista})

def Inicio(req):
   return HttpResponse("Pantalla inicio")

def cursos(req):
   return HttpResponse("Pantalla crusos")

def estudiantes(req):
   return HttpResponse("Pantalla estudiantes")

def profesores(req):
   return HttpResponse("Pantalla profesores")

def entregables(req):
   return HttpResponse("Pantalla entregables")