from django.contrib import admin
from estacionamiento.models import autos, administrador, sistema, personas

# Register your models here.

admin.site.register(autos)
admin.site.register(administrador)
admin.site.register(sistema)
admin.site.register(personas)

