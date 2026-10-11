from rest_framework import serializers
from .models import Trabajador, Turno, HorarioTurno, Programacion, Asistencia, RegistroHistorico


class TrabajadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trabajador
        fields = [
            "id",
            "rut",
            "nombre",
            "cargo",
            "estado",
            "grupo",
            "tipo_turno",
        ]


class TurnoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Turno
        fields = [
            "id",
            "codigo",
            "descripcion",
        ]


class HorarioTurnoSerializer(serializers.ModelSerializer):

    class Meta:
        model = HorarioTurno
        fields = [
            "id",
            "turno",
            "dia",
            "hora_inicio",
            "hora_termino",
        ]


class ProgramacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Programacion
        fields = [
            "id",
            "trabajador",
            "fecha",
            "turno",
        ]


class AsistenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asistencia
        fields = [
            "id",
            "trabajador",
            "fecha",
            "turno",
            "estado",
            "hora_entrada",
            "hora_salida",
            "observacion",
        ]
class RegistroHistoricoSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegistroHistorico
        fields = [
            "id",
            "trabajador_nombre",
            "fecha",
            "hora_entrada",
            "hora_salida",
            "estado",
            "observacion",
        ]
class RegistroHistoricoSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegistroHistorico
        fields = [
            "id",
            "trabajador_nombre",
            "fecha",
            "hora_entrada",
            "hora_salida",
            "estado",
            "observacion",
        ]