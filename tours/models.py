from django.db import models

# Bedutravels/tours/models.py

# Create your models here.
class User(models.Model):
    """ Detinfe la tabla User de nuestro modelo """
    # id <- lo hace Django
    nombre = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    email = models.CharField(max_length=256)
    fechaNacimiento = models.DateField()
    clave = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)
    GENERO =  [
        ("H", "Hombre"),
        ("M", "Mujer"),
        ("O", "Otro"),
        ("N", "Prefiero no indicarlo"),
    ]
    genero =  models.CharField(max_length=1, choices=GENERO)

    def __str__(self):
        """ Representación en cadena para User """
        return self.nombre + " " + self.apellidos

class Zona(models.Model):
    """ Define la tabla Zona """
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=256, null=True, blank=True)
    latitud = models.DecimalField(max_digits=9, decimal_places=7, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=7, null=True, blank=True)

    def __str__(self):
        """ Representación en cadena para zona """
        return self.nombre

class Tour(models.Model):
    """ Define la tabla Tour """
    nombre = models.CharField(max_length=145)
    slug = models.CharField(max_length=45, null=True, blank=True)
    operador = models.CharField(max_length=45, null=True, blank=True)
    tipoDeTour = models.CharField(max_length=45, null=True, blank=True)
    descripcion = models.CharField(max_length=256)
    img = models.CharField(max_length=256, null=True, blank=True)
    pais = models.CharField(max_length=45, null=True, blank=True)
    zonaSalida = models.ForeignKey(Zona, on_delete=models.SET_NULL, null=True,
        blank=True, related_name="tours_salida")
    zonaLlegada = models.ForeignKey(Zona, on_delete=models.SET_NULL, null=True,
        blank=True, related_name="tours_llegada")

    def __str__(self):
        return "{}".format(self.nombre)
