from django.shortcuts import render
from AppBiblio.models import *
from AppBiblio.forms import *
#from tkinter import *
#from tkinter import messagebox as MessageBox


# Create your views here.
from django.http import HttpResponse



def inicio(request):
     return render(request, "AppBiblio/inicio.html")

def biblioteca(request):
     return render(request, "AppBiblio/biblioteca.html")
 
def prestamo(request):
     return render(request, "AppBiblio/prestamos.html")

def usuario(request):
     return render(request, "AppBiblio/usuario.html")


#para mostrar las paginas

def ver_libros(request):
    todos= Libro.objects.all()
    return render(request, "AppBiblio/ver_libros.html", {"todos":todos})

def cargar_libro(request):
    if request.method == "POST":
        miFormulario = libroFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            libro = Libro(titulo=informacion["titulo"],autor=informacion["autor"],editorial=informacion["editorial"],inventario=informacion["inventario"])
            libro.save()
            #MessageBox.showwarning("Alerta", "Sección sólo para administradores.") # título, mensaje
            miFormulario = libroFormulario()# Esto es para que devuelva el formulario limpio
            return render(request, "AppBiblio/cargar_libro.html",{"miFormulario": miFormulario})    #retornamos al formulario
           
    else:
        miFormulario = libroFormulario()
            
    return render(request, "AppBiblio/cargar_libro.html",{"miFormulario": miFormulario})     


def buscar_usuario(request):
    return render(request, "AppBiblio/buscar_usuario.html")

def resultados2 (request):
    if request.GET['nombre']:
        nombreBusqueda = request.GET['nombre']
        resultadoUsuarios = Usuario.objects.filter(nombre__icontains=nombreBusqueda)
    
        return render(request, "AppBiblio/resultados2.html",{"nombreBusqueda":nombreBusqueda, "resultado": resultadoUsuarios})
    else:
        respuesta = "No enviaste Datos"
        return HttpResponse(respuesta)
    
    
    
def buscar_Libro(request):
    return render(request, "AppBiblio/buscar_libro.html")

def resultados (request):
    if request.GET['titulo']:
        tituloBusqueda = request.GET['titulo']
        resultadoLibros = Libro.objects.filter(titulo__icontains=tituloBusqueda)
    
        return render(request, "AppBiblio/resultados.html",{"tituloBusqueda":tituloBusqueda, "resultado": resultadoLibros})
    else:
        respuesta = "No enviaste Datos"
        return HttpResponse(respuesta)
    
def ver_usuarios(request):
    todos= Usuario.objects.all()
    return render(request, "AppBiblio/ver_usuarios.html", {"todos":todos})

def cargar_usuario(request):
    if request.method == "POST":
        miFormulario = usuarioFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario = Usuario(nombre=informacion["nombre"],apellido=informacion["apellido"],Ingreso=informacion["Ingreso"],documento=informacion["documento"])
            usuario.save()
            miFormulario = usuarioFormulario()# Esto es para que devuelva el formulario limpio
            return render(request, "AppBiblio/cargar_usuario.html",{"miFormulario": miFormulario})    #retornamos al formulario
           
    else:
        miFormulario = usuarioFormulario()
            
    return render(request, "AppBiblio/cargar_usuario.html",{"miFormulario": miFormulario})   


def ver_prestamos(request):
    todos= Prestamo.objects.all()
    return render(request, "AppBiblio/ver_prestamos.html", {"todos":todos})  

def cargar_prestamo(request):
    if request.method == "POST":
        miFormulario = cargarPrestamo(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            prestamo = Prestamo(lib=informacion["inventario"],user=informacion["documento"],fecha=informacion["fecha"])
            prestamo.save()
            miFormulario = cargarPrestamo()# Esto es para que devuelva el formulario limpio
            return render(request, "AppBiblio/cargar_prestamo.html",{"miFormulario": miFormulario})    #retornamos al formulario
           
    else:
        miFormulario = cargarPrestamo()
            
    return render(request, "AppBiblio/cargar_prestamo.html",{"miFormulario": miFormulario})   

def cargar_devolucion(request):
    return render(request, "AppBiblio/cargar_devolucion.html")

def resultados3 (request):
    if request.GET['inventario']:
        inventarioBusqueda = request.GET['inventario']
        obj = Prestamo.objects.get(lib=inventarioBusqueda)
        obj.devuelto = True
        obj.save()
        return render(request, "AppBiblio/resultados3.html",{"inventarioBusqueda":inventarioBusqueda, "res": obj})
    else:
        respuesta = "No enviaste Datos"
        return HttpResponse(respuesta)
