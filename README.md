# Sistema-Asistencia

Sistema web desarrollado con Django para gestionar la planificación y el registro de asistencia de trabajadores.

La aplicación permite administrar trabajadores, turnos, horarios y programaciones, registrar la asistencia diaria y mantener un registro histórico de las asistencias.

## Descripción del proyecto

Sistema-Asistencia es una aplicación web desarrollada con Django orientada a facilitar la gestión de asistencia de trabajadores de acuerdo con la programación y los turnos asignados.

El sistema integra una interfaz web con una base de datos MariaDB y una API REST desarrollada utilizando Django REST Framework.

## Objetivo

Desarrollar una solución Back End utilizando Django que permita:

* Administrar trabajadores.
* Administrar turnos.
* Administrar horarios asociados a los turnos.
* Crear y consultar programaciones.
* Registrar la asistencia diaria.
* Mantener un registro histórico de las asistencias.
* Exponer la información mediante una API REST.
* Persistir la información en una base de datos MariaDB.

## Tecnologías utilizadas

* Python
* Django
* Django REST Framework
* MariaDB
* HTML
* CSS
* Git
* GitHub
* JSON Web Token (JWT)

## Funcionalidades principales

### Gestión de trabajadores

Permite almacenar información de los trabajadores:

* RUT
* Nombre
* Cargo
* Estado
* Grupo
* Tipo de turno

### Gestión de turnos

Permite administrar los turnos utilizados por la organización.

Cada turno posee:

* Código
* Descripción

### Gestión de horarios

Permite asociar un horario a un turno según el día de la semana.

Cada horario considera:

* Turno
* Día
* Hora de inicio
* Hora de término

### Planificación

Permite visualizar la programación de trabajadores considerando:

* Fecha
* Trabajador
* Cargo
* Grupo
* Turno
* Horario correspondiente

### Registro de asistencia

Permite registrar:

* Estado de asistencia
* Hora de entrada
* Hora de salida
* Observaciones

Los estados utilizados por el sistema pueden incluir:

* Presente
* Ausente
* Licencia
* Permiso

### Registro histórico

El sistema genera o actualiza un registro histórico asociado al trabajador y a la fecha de asistencia.

El registro histórico conserva:

* Nombre del trabajador
* Fecha
* Hora de entrada
* Hora de salida
* Estado
* Observación

## API REST

El proyecto incorpora una API REST utilizando Django REST Framework.

### API Root

```text
/api/v1/
```

### Endpoints disponibles

```text
/api/v1/trabajadores/
/api/v1/turnos/
/api/v1/horarios/
/api/v1/programaciones/
/api/v1/asistencias/
/api/v1/historicos/
```

Los recursos utilizan ViewSets y `DefaultRouter`.

### Operaciones HTTP

Los ViewSets permiten trabajar con operaciones HTTP estándar:

* GET
* POST
* PUT
* PATCH
* DELETE

Durante la validación funcional se probaron directamente las operaciones sobre el recurso `trabajadores`.

Resultados obtenidos:

```text
GET     → 200 OK
POST    → 201 Created
PATCH   → 200 OK
DELETE  → 204 No Content

## Arquitectura del proyecto

La aplicación utiliza la arquitectura MVT de Django.

### Models

Define las estructuras de datos y relaciones entre:

* Trabajadores
* Turnos
* Horarios
* Programaciones
* Asistencias
* Registros históricos

### Views

Gestiona:

* La lógica de planificación.
* El registro de asistencia.
* La persistencia de los datos.
* La generación y actualización del registro histórico.
* Los ViewSets utilizados por la API REST.

### Serializers

Permiten transformar los modelos Django en representaciones JSON y validar los datos utilizados por la API REST.

### Templates

Contienen las interfaces HTML utilizadas para:

* Planificación semanal.
* Registro de asistencia diaria.

### URLs

Gestionan las rutas de la aplicación web y los endpoints de la API REST.

## Base de datos

El proyecto utiliza MariaDB.

Durante las pruebas se trabajó con MariaDB 10.4.32.

Debido a una incompatibilidad relacionada con la recuperación de columnas generadas durante operaciones de inserción, se incorporó un backend personalizado basado en el backend MySQL de Django.

La configuración utiliza:

```python
can\_return\_columns\_from\_insert = False
```

La conexión con MariaDB fue comprobada desde Django y se verificó el funcionamiento de las operaciones CRUD.

## Validación y pruebas

El proyecto fue validado mediante pruebas locales.

Se utilizó:

```bash
python manage.py check
```

Resultado final:

```text
System check identified no issues (0 silenced).
```

### Pruebas de API

Se verificaron las operaciones CRUD de:

* Trabajadores
* Turnos
* Horarios
* Programaciones
* Asistencias
* Registro histórico

También se verificaron las consultas individuales mediante identificador.

### Prueba de integración

Se comprobó el flujo completo de la aplicación:

```text
Planificación
      ↓
Programación
      ↓
Registro de asistencia
      ↓
Guardar asistencia
      ↓
Asistencia en base de datos
      ↓
Registro histórico
```

La prueba final confirmó la persistencia de los datos tanto en `Asistencia` como en `RegistroHistorico`.

Durante la validación final se comprobó la existencia de registros en las entidades principales:

```text
Trabajadores: 1
Turnos: 1
Horarios: 1
Programaciones: 1
Asistencias: 1
Historicos: 1
```

## Uso de Inteligencia Artificial (IA)

Durante el desarrollo del proyecto se utilizó Inteligencia Artificial como herramienta de apoyo al aprendizaje, programación, análisis, resolución de problemas y documentación.

La IA fue utilizada como copiloto durante distintas etapas del desarrollo.

### Acciones realizadas con apoyo de IA

La Inteligencia Artificial fue utilizada para:

* Comprender conceptos relacionados con Django y Django REST Framework.
* Orientar la estructura de modelos, vistas, serializers y rutas.
* Apoyar la implementación de ViewSets y endpoints de la API REST.
* Analizar mensajes de error generados durante la ejecución del proyecto.
* Proponer soluciones frente a errores de configuración y programación.
* Revisar estructuras de código Python.
* Apoyar la integración entre la interfaz web y la base de datos.
* Proponer y revisar pruebas de funcionamiento de la API.
* Apoyar la documentación técnica del proyecto.
* Orientar el uso de Git y GitHub.

### Auditoría y validación del código generado con IA

Las propuestas generadas mediante Inteligencia Artificial fueron revisadas antes de incorporarse al proyecto.

El proceso seguido fue:

1. Solicitar una propuesta de solución.
2. Revisar el código y su funcionamiento esperado.
3. Implementar la solución en el proyecto.
4. Ejecutar el código en el entorno local.
5. Analizar los errores encontrados.
6. Corregir las propuestas cuando fue necesario.
7. Realizar nuevamente las pruebas.
8. Validar finalmente el funcionamiento mediante Django y la base de datos.

Durante este proceso se detectaron y solucionaron errores como:

* ViewSets que no estaban registrados correctamente en el router.
* Serializers faltantes o imports incorrectos.
* Registro duplicado de un `basename`.
* Problemas relacionados con las rutas de la API.
* Problemas de compatibilidad entre Django y MariaDB.
* Diferencias entre los identificadores utilizados durante las pruebas y los registros existentes en la base de datos.
* Ausencia inicial de la generación automática del registro histórico.
* Manejo incorrecto del valor `"None"` como texto en las observaciones.

Estos casos fueron utilizados para revisar, modificar y validar las propuestas antes de considerar las soluciones como definitivas.

La Inteligencia Artificial fue utilizada como herramienta de apoyo y no como sustituto del desarrollo ni de la toma de decisiones técnicas.

La implementación final fue comprobada mediante ejecución local, pruebas funcionales, consultas a la base de datos y `python manage.py check`.

## Control de versiones

El proyecto utiliza Git para el control de versiones y GitHub como repositorio remoto.

Repositorio:

[https://github.com/Marilu-lu/Sistema-Asistencia.git](https://github.com/Marilu-lu/Sistema-Asistencia.git)

## Instalación

### Clonar el repositorio

```bash
git clone https://github.com/Marilu-lu/Sistema-Asistencia.git
```

### Ingresar al proyecto

```bash
cd Sistema-Asistencia
```

### Crear el entorno virtual

```bash
python -m venv .venv
```

### Activar el entorno virtual en Windows

```powershell
.venv\\Scripts\\activate
```

### Instalar las dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar las migraciones

```bash
python manage.py migrate
```

### Ejecutar el servidor

```bash
python manage.py runserver
```

La aplicación estará disponible en:

```text
http://127.0.0.1:8000/
```

La API estará disponible en:

```text
http://127.0.0.1:8000/api/v1/
```

## Estado del proyecto

Proyecto funcional y validado localmente.

Se verificó:

* Conexión con MariaDB.
* Funcionamiento de Django.
* Funcionamiento de Django REST Framework.
* API REST.
* Operaciones CRUD.
* Planificación.
* Registro de asistencia.
* Generación del registro histórico.
* Persistencia de datos.
* Validación mediante `python manage.py check`.

Resultado final:

```text
System check identified no issues (0 silenced).


