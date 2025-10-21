from django.contrib import admin
from .models import Especialidad, Medico, Paciente, Consulta, Medicamento, Receta, Tratamiento

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'rut', 'especialidad')
    search_fields = ('nombre', 'apellido', 'rut')
    list_filter = ('especialidad',)

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'rut', 'edad', 'sexo')
    search_fields = ('nombre', 'rut')
    list_filter = ('sexo',)

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id', 'medico', 'paciente', 'fecha', 'motivo')
    search_fields = ('paciente__nombre', 'medico__nombre', 'motivo')
    list_filter = ('fecha', 'medico')

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'consulta', 'medicamento', 'indicaciones')
    search_fields = ('consulta__paciente__nombre', 'medicamento__nombre')

@admin.register(Tratamiento)
class TratamientoAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente', 'medico', 'descripcion', 'fecha_inicio', 'activo')
    search_fields = ('paciente__nombre', 'medico__nombre')
    list_filter = ('activo', 'fecha_inicio')
