from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import alumno, materia, Docente
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def saludo(request):
    return  HttpResponse("Hola desde django")

def edad(request, edad):
    return HttpResponse("Hola tu edad es: "+ str(edad))

def index(request):
    return render(request, 'index.html')

# ALUMNOS---------------------------------------------------------------------------------

def alumnos(request):
    return render(request, 'alumnos.html')

@csrf_exempt
def save_alumno(request):
    datos = json.loads(request.body)
    accion = datos.get ("accion")
    idA = datos.get("idAlumno")
    cod = datos.get("codigo")
    nom = datos.get("nombre")
    dir = datos.get("direccion")
    tel = datos.get("telefono")
    
    if accion=="nuevo":
        editAlumno =alumno.objects.create(codigo=cod, nombre=nom, direccion=dir, telefono=tel)
    elif accion=="modificar":
        editAlumno = alumno.objects.get(id=idA)
        editAlumno.codigo=cod
        editAlumno.nombre=nom
        editAlumno.direccion=dir
        editAlumno.telefono=tel
        editAlumno.save()
    elif accion=="eliminar":
        editAlumno = alumno.objects.get(id=idA)
        editAlumno.delete()
    return JsonResponse({'msg':'ok', 'idAlumno':editAlumno.id}, safe=False)
        
    
def busqueda_alumnos(request):
    return render(request, 'busqueda_alumnos.html')

@csrf_exempt
def buscar_alumnos(request):
    datos= alumno.objects.values('id','codigo','nombre','direccion','telefono')
    return JsonResponse (list(datos), safe=False)

# MATERIAS---------------------------------------------------------------------------------

def materias(request):
    return render(request, 'materias.html')

@csrf_exempt
def save_materias(request):
    datos = json.loads(request.body)
    accion = datos.get ("accion")
    idM = datos.get("idMateria")
    cod = datos.get("codigo")
    nom = datos.get("nombre")
    uvm = datos.get("uv")
    
    if accion=="nuevo":
        editMateria =materia.objects.create(codigo=cod, nombre=nom, uv=uvm)
    elif accion=="modificar":
        editMateria = materia.objects.get(id=idM)
        editMateria.codigo=cod
        editMateria.nombre=nom
        editMateria.uv=uvm
        editMateria.save()
    elif accion=="eliminar":
        editMateria = materia.objects.get(id=idM)
        editMateria.delete()
    return JsonResponse({'msg':'ok', 'idMateria':editMateria.id}, safe=False)
        
    
def busqueda_materias(request):
    return render(request, 'busqueda_materias.html')

@csrf_exempt
def buscar_materias(request):
    datos= materia.objects.values('id','codigo','nombre','uv')
    return JsonResponse (list(datos), safe=False)

#DOCENTES---------------------------------------------------------------------------------

def docentes(request):
    return render(request, 'docentes.html')

@csrf_exempt
def save_docentes(request):
    datos = json.loads(request.body)
    accion = datos.get ("accion")
    idD = datos.get("idDocentes")
    cod = datos.get("codigo")
    nom = datos.get("nombre")
    tel = datos.get("telefono")
    
    if accion=="nuevo":
        editDocentes =Docente.objects.create(codigo=cod, nombre=nom, telefono=tel)
    elif accion=="modificar":
        editDocentes = Docente.objects.get(id=idD)
        editDocentes.codigo=cod
        editDocentes.nombre=nom
        editDocentes.telefono=tel
        editDocentes.save()
    elif accion=="eliminar":
        editDocentes = Docente.objects.get(id=idD)
        editDocentes.delete()
    return JsonResponse({'msg':'ok', 'idDocentes':editDocentes.id}, safe=False)
        
    
def busqueda_docentes(request):
    return render(request, 'busqueda_docentes.html')

@csrf_exempt
def buscar_docentes(request):
    datos= Docente.objects.values('id','codigo','nombre','telefono')
    return JsonResponse (list(datos), safe=False)