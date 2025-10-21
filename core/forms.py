from django import forms
from .models import Medico, Paciente, Consulta, Receta


# ------------------ MÉDICO ------------------
class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nombre', 'apellido', 'rut', 'especialidad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad': forms.Select(attrs={'class': 'form-control'}),
        }


# ------------------ PACIENTE ------------------
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'rut', 'edad', 'sexo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
        }


# ------------------ CONSULTA ------------------
class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['medico', 'paciente', 'fecha', 'motivo']
        widgets = {
            'medico': forms.Select(attrs={'class': 'form-select'}),
            'paciente': forms.Select(attrs={'class': 'form-select'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


# ------------------ RECETA ------------------
class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['consulta', 'medicamento', 'indicaciones']
        widgets = {
            'consulta': forms.Select(attrs={'class': 'form-select'}),
            'medicamento': forms.Select(attrs={'class': 'form-select'}),
            'indicaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
