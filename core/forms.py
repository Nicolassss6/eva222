from django import forms
from .models import Medico, Paciente, Consulta, Receta

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nombre','apellido','rut','telefono','especialidad']

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre','apellido','rut','fecha_nacimiento','telefono','direccion']

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['medico','paciente','fecha','motivo','diagnostico']

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['consulta','medicamento','dosis','instrucciones']
