from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='estudiantes'), name='inicio'),
    path('estudiantes/', views.lista_estudiantes, name='estudiantes'),
    path('cursos/', views.lista_cursos, name='cursos'),
]