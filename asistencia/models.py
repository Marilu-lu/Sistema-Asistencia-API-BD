from django.db import models


class Trabajador(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    estado = models.CharField(max_length=20)

    grupo = models.CharField(
        max_length=1,
        null=True,
        blank=True
    )

    tipo_turno = models.CharField(
    max_length=20,
    null=True,
    blank=True

    )

    class Meta:
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"

    def __str__(self):
        return self.nombre


class Turno(models.Model):
    codigo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"

    def __str__(self):
        return self.codigo


class HorarioTurno(models.Model):
    turno = models.ForeignKey(
        Turno,
        on_delete=models.CASCADE,
        null = True,
        blank = True
        
    )

    dia = models.CharField(max_length=15)

    hora_inicio = models.TimeField()

    hora_termino = models.TimeField()

    class Meta:
        verbose_name = "Horario de turno"
        verbose_name_plural = "Horarios de turnos"

    def __str__(self):
        return f"{self.turno.codigo} - {self.dia}"


class Programacion(models.Model):
    trabajador = models.ForeignKey(
        Trabajador,
        on_delete=models.CASCADE
    )

    fecha = models.DateField()

    turno = models.ForeignKey(
        Turno,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.trabajador.nombre} | {self.fecha} | {self.turno.codigo}"

    class Meta:
       verbose_name = "Programación"
       verbose_name_plural = "Programaciones"
       ordering = ["fecha"]
    
    
class Asistencia(models.Model):

    trabajador = models.ForeignKey(
        Trabajador,
        on_delete=models.CASCADE
    )

    fecha = models.DateField()

    turno = models.ForeignKey(
        Turno,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    estado = models.CharField(max_length=30)

    hora_entrada = models.TimeField(
        null=True,
        blank=True
    )

    hora_salida = models.TimeField(
        null=True,
        blank=True
    )

    observacion = models.TextField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.trabajador.nombre} | {self.fecha} | {self.turno.codigo if self.turno else 'Sin turno'} | {self.estado}"
    
class RegistroHistorico(models.Model):

    trabajador_nombre = models.CharField(
        max_length=100
    )

    fecha = models.DateField()

    hora_entrada = models.TimeField(
        null=True,
        blank=True
    )

    hora_salida = models.TimeField(
        null=True,
        blank=True
    )

    estado = models.CharField(
        max_length=30
    )

    observacion = models.TextField(
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Registro histórico"
        verbose_name_plural = "Registros históricos"

    def __str__(self):
        return f"{self.trabajador_nombre} | {self.fecha}"