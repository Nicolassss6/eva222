from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Medico, Especialidad, Paciente, Consulta, Medicamento, Tratamiento
from .forms import MedicoForm, PacienteForm, ConsultaForm

# MEDICO
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

# PACIENTE
class PacienteListView(ListView):
    model = Paciente
    template_name = 'paciente_list.html'
    paginate_by = 10

class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente_form.html'
    success_url = reverse_lazy('paciente_list')

# ESPECIALIDAD
class EspecialidadListView(ListView):
    model = Especialidad
    template_name = 'especialidad_list.html'

# CONSULTA
class ConsultaListView(ListView):
    model = Consulta
    template_name = 'consulta_list.html'
    paginate_by = 10

class ConsultaCreateView(CreateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'consulta_form.html'
    success_url = reverse_lazy('consulta_list')

# TRATAMIENTO
class TratamientoListView(ListView):
    model = Tratamiento
    template_name = 'tratamiento_list.html'
    paginate_by = 10

def home(request):
    return redirect('medico_list')

# ------------------ RECETA ------------------
from .models import Receta
from .forms import RecetaForm
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


class RecetaListView(ListView):
    model = Receta
    template_name = 'receta_list.html'
    paginate_by = 10


class RecetaCreateView(CreateView):
    model = Receta
    form_class = RecetaForm
    template_name = 'receta_form.html'
    success_url = reverse_lazy('receta_list')

