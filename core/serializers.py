from rest_framework import serializers
from .models import Especialidad, Medico, Paciente, Consulta, Medicamento, Receta, Tratamiento


class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = '__all__'


class MedicoSerializer(serializers.ModelSerializer):
    especialidad = EspecialidadSerializer(read_only=True)
    especialidad_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source='especialidad',
        queryset=Especialidad.objects.all()
    )

    class Meta:
        model = Medico
        fields = ['id', 'nombre', 'apellido', 'rut', 'especialidad', 'especialidad_id']


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'


class ConsultaSerializer(serializers.ModelSerializer):
    medico = MedicoSerializer(read_only=True)
    paciente = PacienteSerializer(read_only=True)
    medico_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source='medico',
        queryset=Medico.objects.all()
    )
    paciente_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source='paciente',
        queryset=Paciente.objects.all()
    )

    class Meta:
        model = Consulta
        fields = ['id', 'medico', 'paciente', 'medico_id', 'paciente_id', 'fecha', 'motivo']


class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'


class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = '__all__'


class TratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = '__all__'
