
from django.contrib import admin
from django.urls import path
from AppCoder.views import curso,lista_cursos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista_cursos/', lista_cursos)
]
