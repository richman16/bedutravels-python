from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # / -> views.index()
    path("perfiles", views.perfiles, name="perfiles"),  # /perfiles -> views.perfiles()
    path("login", views.login_user, name="login"),
    # Rutas para el modelo tour
    # tour/eliminar/ID
    path("tour/eliminar/<int:idTour>", views.tour_eliminar, name="tour_eliminar"),
]  # Lista de rutas de la app -tours-
