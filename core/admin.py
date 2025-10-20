from django.contrib import admin
from .models import Especialidad, Medico, Paciente, Consulta, Medicamento, Receta

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre_completo','rut','especialidad','telefono')
    search_fields = ('nombre','apellido','rut')

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id','nombre_completo','rut','telefono')

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','presentacion')

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id','fecha','paciente','medico')

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('id','consulta','medicamento','dosis')
