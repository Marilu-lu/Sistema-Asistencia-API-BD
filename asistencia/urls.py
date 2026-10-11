from django.urls import path, include

from . import views

from .views import (TrabajadorViewSet,TurnoViewSet,HorarioTurnoViewSet,ProgramacionViewSet, AsistenciaViewSet, RegistroHistoricoViewSet
)

from rest_framework.routers import DefaultRouter


router = DefaultRouter()


router.register(
    r'trabajadores',
    TrabajadorViewSet,
    basename='trabajador'
)


router.register(
    r'turnos',
    TurnoViewSet,
    basename='turno'
)


router.register(
    r'horarios',
    HorarioTurnoViewSet,
    basename='horario-turno'
)

router.register(
    r'programaciones',
    ProgramacionViewSet,
    basename='programacion'
)
router.register(
    r'asistencias',
    AsistenciaViewSet,
    basename='asistencia'
)
router.register(
    r'historicos',
    RegistroHistoricoViewSet,
    basename='registro-historico'
)


urlpatterns = [

    path(
        'planificacion/',
        views.planificacion,
        name='planificacion'
    ),

    path(
        'asistencia/',
        views.asistencia,
        name='asistencia'
    ),

    path(
        'api/v1/',
        include(router.urls)
    ),

]