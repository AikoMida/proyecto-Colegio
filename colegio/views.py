from django.shortcuts import render

from django.shortcuts import render
from .models import Estudiante, Curso


def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'colegio/estudiantes.html', {'estudiantes': estudiantes})


def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'colegio/cursos.html', {'cursos': cursos})