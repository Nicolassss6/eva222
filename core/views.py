from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Medico, Especialidad, Paciente, Consulta, Medicamento, Receta
from .forms import MedicoForm, PacienteForm, ConsultaForm, RecetaForm

class MedicoListView(ListView):
    model = Medico
    template_name = 'medico_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset().select_related('especialidad')
        q = self.request.GET.get('q')
        esp = self.request.GET.get('especialidad')
        if q:
            qs = qs.filter(nombre__icontains=q) | qs.filter(apellido__icontains=q) | qs.filter(rut__icontains=q)
        if esp:
            qs = qs.filter(especialidad_id=esp)
        return qs

class MedicoCreateView(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico_form.html'
    success_url = reverse_lazy('medico_list')

class MedicoUpdateView(UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico_form.html'
    success_url = reverse_lazy('medico_list')

class MedicoDetailView(DetailView):
    model = Medico
    template_name = 'medico_detail.html'

class MedicoDeleteView(DeleteView):
    model = Medico
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('medico_list')

class PacienteListView(ListView):
    model = Paciente
    template_name = 'paciente_list.html'
    paginate_by = 10

class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente_form.html'
    success_url = reverse_lazy('paciente_list')

class EspecialidadListView(ListView):
    model = Especialidad
    template_name = 'especialidad_list.html'

class ConsultaListView(ListView):
    model = Consulta
    template_name = 'consulta_list.html'
    paginate_by = 10

class ConsultaCreateView(CreateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'consulta_form.html'
    success_url = reverse_lazy('consulta_list')

def home(request):
    return redirect('medico_list')
