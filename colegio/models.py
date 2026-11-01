from django.db import models

from django.db import models


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Curso(models.Model):
    nombre_curso = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_curso