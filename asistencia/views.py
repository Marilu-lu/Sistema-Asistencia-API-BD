from django.shortcuts import render
from django.contrib import messages

from .models import (
    Programacion,
    Trabajador,
    Asistencia,
    HorarioTurno,
    Turno,
    RegistroHistorico,
)

from rest_framework import viewsets

from .serializers import (
    TrabajadorSerializer,
    TurnoSerializer,
    HorarioTurnoSerializer,
    ProgramacionSerializer,
    AsistenciaSerializer,
    RegistroHistoricoSerializer,
)


def planificacion(request):

    programaciones = Programacion.objects.all()

    dias = [
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Viernes",
        "Sábado",
        "Domingo"
    ]

    for registro in programaciones:

        dia = dias[registro.fecha.weekday()]

        horario = HorarioTurno.objects.filter(
            turno=registro.turno,
            dia=dia
        ).first()

        registro.horario = horario

    contexto = {
        "programaciones": programaciones
    }

    return render(
        request,
        "asistencia/planificacion.html",
        contexto
    )


def asistencia(request):

    fecha = request.GET.get("fecha")

    error = None

    if request.method == "POST":

        fecha = request.POST.get("fecha")

        programaciones = Programacion.objects.filter(
            fecha=fecha
        )

        estados_faltantes = []

        for registro in programaciones:

            trabajador_id = registro.trabajador.id

            estado = request.POST.get(
                f"estado_{trabajador_id}"
            )

            if not estado:

                estados_faltantes.append(
                    registro.trabajador.nombre
                )

        if estados_faltantes:

            error = (
                "Debe seleccionar un estado para: "
                + ", ".join(estados_faltantes)
            )

        else:

            for registro in programaciones:

                trabajador_id = registro.trabajador.id

                estado = request.POST.get(
                    f"estado_{trabajador_id}"
                )

                hora_entrada = request.POST.get(
                    f"entrada_{trabajador_id}"
                )

                hora_salida = request.POST.get(
                    f"salida_{trabajador_id}"
                )

                observacion = request.POST.get(
                    f"observacion_{trabajador_id}"
                )

                # Convertir valores vacíos o "None"
                # en None real de Python.
                if not observacion or observacion.strip().lower() == "none":
                    observacion = None

                if not hora_entrada:
                    hora_entrada = None

                if not hora_salida:
                    hora_salida = None

                # -----------------------------------
                # GUARDAR ASISTENCIA
                # -----------------------------------

                Asistencia.objects.update_or_create(

                    trabajador=registro.trabajador,

                    fecha=fecha,

                    defaults={

                        "turno": registro.turno,

                        "estado": estado,

                        "hora_entrada": hora_entrada,

                        "hora_salida": hora_salida,

                        "observacion": observacion,

                    }

                )

                # -----------------------------------
                # GUARDAR REGISTRO HISTÓRICO
                # -----------------------------------

                RegistroHistorico.objects.update_or_create(

                    trabajador_nombre=registro.trabajador.nombre,

                    fecha=fecha,

                    defaults={

                        "hora_entrada": hora_entrada,

                        "hora_salida": hora_salida,

                        "estado": estado,

                        "observacion": observacion,

                    }

                )

            messages.success(
                request,
                "Asistencia guardada correctamente."
            )

    # -----------------------------------
    # CARGAR PROGRAMACIONES
    # -----------------------------------

    if fecha:

        programaciones = Programacion.objects.filter(
            fecha=fecha
        )

    else:

        programaciones = Programacion.objects.none()

    # -----------------------------------
    # CARGAR ASISTENCIA EXISTENTE
    # -----------------------------------

    for registro in programaciones:

        registro.asistencia = Asistencia.objects.filter(
            trabajador=registro.trabajador,
            fecha=fecha
        ).first()

    contexto = {

        "trabajadores": Trabajador.objects.all(),

        "programaciones": programaciones,

        "fecha": fecha,

        "error": error,

    }

    return render(
        request,
        "asistencia/asistencia.html",
        contexto
    )


# ==========================================
# API REST
# ==========================================

class TrabajadorViewSet(viewsets.ModelViewSet):

    queryset = Trabajador.objects.all()

    serializer_class = TrabajadorSerializer


class TurnoViewSet(viewsets.ModelViewSet):

    queryset = Turno.objects.all()

    serializer_class = TurnoSerializer


class HorarioTurnoViewSet(viewsets.ModelViewSet):

    queryset = HorarioTurno.objects.all()

    serializer_class = HorarioTurnoSerializer


class ProgramacionViewSet(viewsets.ModelViewSet):

    queryset = Programacion.objects.all()

    serializer_class = ProgramacionSerializer


class AsistenciaViewSet(viewsets.ModelViewSet):

    queryset = Asistencia.objects.all()

    serializer_class = AsistenciaSerializer


class RegistroHistoricoViewSet(viewsets.ModelViewSet):

    queryset = RegistroHistorico.objects.all()

    serializer_class = RegistroHistoricoSerializer