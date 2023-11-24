from django.contrib import admin
from django.urls import path
from appalumnos.views import saludo, edad, index, alumnos, busqueda_alumnos, save_alumno, buscar_alumnos, materias, save_materias, busqueda_materias, buscar_materias, docentes, save_docentes, busqueda_docentes, buscar_docentes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('edad/<int:edad>',edad),
    path('', index),
    
    #URL de alumnos
    path('frmalumnos', alumnos),
    path('alumnos', save_alumno),
    path('frmbusqueda_alumnos', busqueda_alumnos),
    path('buscar_alumnos', buscar_alumnos),
    
    #URL de materia
    path('frmmaterias', materias),
    path('materias', save_materias),
    path('frmbusqueda_materias', busqueda_materias),
    path('buscar_materias', buscar_materias),
    
    #URL de docentes
    path('frmdocentes', docentes),
    path('docentes', save_docentes),
    path('frmbusqueda_docentes', busqueda_docentes),
    path('buscar_docentes', buscar_docentes),
]
