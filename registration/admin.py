from django.contrib import admin
from .models import Cliente, Persona, Empleado


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    pass


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    pass
