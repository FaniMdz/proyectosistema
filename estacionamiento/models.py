from django.db import models
from django.db.models.fields import AutoField

# Create your models here.

class administrador(models.Model):
    Id_admin = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__ (self):
       return (self.usuario)   

class sistema(models.Model):
    Id_color = models.AutoField(primary_key=True)
    color = models.CharField(max_length=30)

    def __str__ (self):
       return (self.color)    
    
class personas(models.Model):
    Id_persona = models.AutoField(primary_key=True),
    Id_color = models.ForeignKey(sistema, null=False, blank=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    ap_pat = models.CharField(max_length=30)
    ap_mat = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)

    def __str__ (self):
       return (self.nombre)

class autos(models.Model):
    Id_auto = models.AutoField(primary_key=True)
    Id_color = models.ForeignKey(sistema, null=False, blank=False, on_delete=models.CASCADE)
    fecha = models.DateField()
    horaE = models.TimeField()
    horaS = models.TimeField()
    descripcion = models.CharField(max_length=60)
    Id_admin = models.ForeignKey(administrador, null=False, blank=False, on_delete=models.CASCADE)

    def __str__ (self):
       return (self.descripcion)
