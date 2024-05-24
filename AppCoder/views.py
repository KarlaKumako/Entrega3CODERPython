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
   return render(req,"Inicio.html",{})

def cursos(req):
   return render(req,"cursos.html",{})

def estudiantes(req):
   return render(req,"estudiantes.html",{})

def profesores(req):
   return render(req,"profesores.html",{})

def entregables(req):
   return render(req,"entregables.html",{})