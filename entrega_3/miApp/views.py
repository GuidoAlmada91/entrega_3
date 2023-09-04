from django.shortcuts import render
from .models import Curso
from .forms import CursoFormulario

# Create your views here.

def inicio(request):
    return render(request, "miApp/inicio.html")

def cursos_view(request):
     if request.method == "GET":
         print("+" * 90) #  Imprimimos esto para ver por consola
         print("+" * 90) #  Imprimimos esto para ver por consola
         return render(
             request,
             "miApp/curso_formulario_avanzado.html",
             {"form": CursoFormulario()}
         )
     else:
         print("*" * 90)     #  Imprimimos esto para ver por consola
         print(request.POST) #  Imprimimos esto para ver por consola
         print("*" * 90)     #  Imprimimos esto para ver por consola
         modelo = Curso(curso=request.POST["curso"], camada=request.POST["camada"])
         modelo.save()
         return render(
             request,
             "miApp/inicio.html",
         )


        

def cursos_enriquecido(request):
    return render(
        request, 
        "miApp/cursos_enriquecido.html",
        {"nombre": "Guido", "apellido": "Almada"}
        )

#def cursos_formulario(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST)
        #Podemos crear un curso
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "miApp/inicio.html")
        else:
            # Si el formulario no es válido, renderiza el formulario nuevamente con los errores
            return render(request, "miApp/curso_formulario.html", {"form": mi_formulario})
    else:
        mi_formulario = CursoFormulario()
        return render(request, "miApp/curso_formulario.html", {"form": mi_formulario})
    

def profesor(request):
    return render(request, "miApp/profesor.html")
def estudiante(request):
    return render(request, "miApp/estudiante.html")
def entregable(request):
    return render(request, "miApp/entregable.html")
