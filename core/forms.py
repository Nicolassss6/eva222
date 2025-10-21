from django import forms
from .models import Medico, Paciente, Consulta, Receta

# --- MÉDICO ---
class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nombre', 'apellido', 'rut', 'especialidad']

# --- PACIENTE ---
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'rut', 'edad', 'sexo']

# --- CONSULTA ---
class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['medico', 'paciente', 'fecha', 'motivo']

# --- RECETA ---
class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['consulta', 'medicamento', 'indicaciones']
