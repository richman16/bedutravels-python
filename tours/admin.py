from django.contrib import admin
from .models import User, Zona, Tour

# Bedutravels/tours/admin.py

class ZonaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "descripcion", "longitud", "latitud")

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "apellidos", "email", "fechaNacimiento", "genero")

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Zona, ZonaAdmin)

class TourAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "descripcion", "zonaSalida", "zonaLlegada")

# Register your models here.
admin.site.register(Tour, TourAdmin)


