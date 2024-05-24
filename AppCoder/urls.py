
from django.contrib import admin
from django.urls import path
from AppCoder.views import curso,lista_cursos,Inicio,cursos,profesores,estudiantes,entregables

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista_cursos/', lista_cursos),
    path('', lista_cursos),
    path('cursos/', cursos),
    path('estudiantes/', estudiantes),
    path('profesores/', profesores),
    path('entregables/', entregables),
]
