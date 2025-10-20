from django.db import models

class Especialidad(models.Model):
    nombre = models.CharField(max_length=120)

    def __str__(self):
        return self.nombre

class Medico(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    rut = models.CharField(max_length=12, unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True, related_name='medicos')

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        return self.nombre_completo

class Paciente(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    rut = models.CharField(max_length=12, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        return self.nombre_completo

class Medicamento(models.Model):
    nombre = models.CharField(max_length=150)
    presentacion = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.nombre

class Consulta(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='consultas')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    fecha = models.DateTimeField()
    motivo = models.TextField(blank=True)
    diagnostico = models.TextField(blank=True)

    def __str__(self):
        return f"Consulta {self.id} - {self.paciente.nombre_completo} / {self.medico.nombre_completo}"

class Receta(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, related_name='recetas')
    medicamento = models.ForeignKey(Medicamento, on_delete=models.SET_NULL, null=True)
    dosis = models.CharField(max_length=120, blank=True)
    instrucciones = models.TextField(blank=True)

    def __str__(self):
        return f"Receta {self.id} - {self.medicamento}"
