from django.core.management.base import BaseCommand
from asistencia.models import Trabajador, Turno, Programacion
from datetime import date


class Command(BaseCommand):
    help = "Crea programación semanal de prueba"

    def handle(self, *args, **kwargs):

        semana = [
            date(2026, 7, 6),
            date(2026, 7, 7),
            date(2026, 7, 8),
            date(2026, 7, 9),
            date(2026, 7, 10),
        ]

        turno_am = Turno.objects.get(codigo="AM")
        turno_pm = Turno.objects.get(codigo="PM")

        grupo_a = Trabajador.objects.filter(grupo="A")
        grupo_b = Trabajador.objects.filter(grupo="B")

        for trabajador in grupo_a:
            for dia in semana:
                Programacion.objects.create(
                    trabajador=trabajador,
                    fecha=dia,
                    turno=turno_am
                )

        for trabajador in grupo_b:
            for dia in semana:
                Programacion.objects.create(
                    trabajador=trabajador,
                    fecha=dia,
                    turno=turno_pm
                )

        self.stdout.write(
            self.style.SUCCESS(
                "Programación creada correctamente"
            )
        )
