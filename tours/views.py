from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Tour, User

# Create your views here.
@login_required()
def index(request):
    """ Atiende la petición GET / """

    lista_tours = Tour.objects.all()
    ntours = len(lista_tours)

    # Consutlar si el usuario pertene al grupo editores

    user = request.user
    # Esto regresa una lista de resultados
    es_editor = user.groups.filter(name="Editores").exists()

    return render(request, "tours/index.html",
        {"tours":lista_tours, "ntours":ntours, "es_editor": es_editor}
    )  # templates/tours/index.html

def perfiles(request):
    """ Atiende la petición GET /perfiles """
    return render(request, "tours/perfil.html")  # templates/tours/perfil.html

def login_user(request):
    """ Atiende la petición GET /login """
    msg = ""

    # Obtener los datos del formulario
    if request.method == "POST":
        user_form = (request.POST["username"], request.POST["password"])
        next_url = request.GET.get("next", "/")
        user = authenticate(username = user_form[0], password=user_form[1])
        if user is not None:
            # Se inicializan las variables de sesion
            login(request, user)
            return redirect(next_url)
        else:
            msg = "Datos de acceso inválidos"

    return render(request, "registration/login.html", { "msg": msg })

def tour_eliminar(request, idTour):
    """ Atiende la peticion GET /tour/eliminar/<ID> """
    tour = Tour.objects.get(pk=idTour)
    tour.delete()
    return redirect("index")
