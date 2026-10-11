from django.contrib import admin
from .models import Trabajador, Turno, HorarioTurno, Programacion, Asistencia


admin.site.register(Trabajador)
admin.site.register(Turno)
admin.site.register(HorarioTurno)
admin.site.register(Programacion)
admin.site.register(Asistencia)