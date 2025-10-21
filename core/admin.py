from django.contrib import admin
from .models import Medico, Especialidad, Paciente, Consulta, Medicamento, Receta, Tratamiento


# ------------------ MÉDICO ------------------
@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'rut', 'especialidad')
    search_fields = ('nombre', 'apellido', 'rut')
    list_filter = ('especialidad',)


# ------------------ PACIENTE ------------------
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'rut', 'edad', 'sexo')
    search_fields = ('nombre', 'rut')
    list_filter = ('sexo',)


# ------------------ ESPECIALIDAD ------------------
@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


# ------------------ CONSULTA ------------------
@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id', 'medico', 'paciente', 'fecha', 'motivo')
    search_fields = ('paciente__nombre', 'medico__nombre')
    list_filter = ('fecha', 'medico')


# ------------------ MEDICAMENTO ------------------
@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)


# ------------------ RECETA ------------------
@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'consulta', 'medicamento', 'indicaciones')
    search_fields = ('medicamento__nombre', 'consulta__paciente__nombre')


# ------------------ TRATAMIENTO ------------------
@admin.register(Tratamiento)
class TratamientoAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente', 'medico', 'descripcion', 'activo')
    search_fields = ('paciente__nombre', 'medico__nombre')
    list_filter = ('activo',)
