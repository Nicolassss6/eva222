from rest_framework import viewsets
from .models import Especialidad, Medico, Paciente, Consulta, Medicamento, Receta
from .serializers import (EspecialidadSerializer, MedicoSerializer, PacienteSerializer,
                          ConsultaSerializer, MedicamentoSerializer, RecetaSerializer)

class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.select_related('especialidad').all()
    serializer_class = MedicoSerializer
    filterset_fields = ['especialidad']

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.select_related('medico','paciente').all()
    serializer_class = ConsultaSerializer
    filterset_fields = ['medico','paciente','fecha']

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.select_related('medicamento','consulta').all()
    serializer_class = RecetaSerializer
