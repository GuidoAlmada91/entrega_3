"""
URL configuration for entrega_3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import cursos_view, inicio



urlpatterns = [
    #path('cursos_enriquecido/', cursos_enriquecido),
    #path('cursos_formulario/', cursos_formulario),
    path('inicio', inicio),
    path('cursos/', cursos_view),
    #path('profesor/', views.profesor, name="profesor"),
    #path('estudiante/', views.estudiante, name="estudiante"),
    #path('entregable/', views.entregable, name="entregable"),

]
