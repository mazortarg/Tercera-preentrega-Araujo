from django.urls import path
from AppBiblio.views import * #trae todas las funciones de views

urlpatterns = [
    
    path('inicio/',inicio, name="Inicial"),
    
    path('Usuarios',usuario, name="Usuarios"),
    path('verUsuarios',ver_usuarios, name="verUsuarios"),
    path('cargarUsuarios',cargar_usuario, name="cargarUsuarios"),
    path('buscarUsuarios',buscar_usuario, name="buscarUsuarios"),
    path('resultado2',resultados2),
    
    path('Biblioteca',biblioteca, name="Biblioteca"),
    path('verlibros/',ver_libros, name="verLibros"),
    path('cargarlibros', cargar_libro, name="cargarLibro"),
    path('buscarlibro', buscar_Libro, name="buscarLibro"),
    path('resultado',resultados),
    
    path('Prestamos',prestamo, name="Prestamos"),
    path('verPrestamos',ver_prestamos, name="verPrestamos"),
    path('cargarPrestamos',cargar_prestamo, name="cargarPrestamos"),
    path('cargarDevolucion',cargar_devolucion, name="cargarDevolucion"),
    path('resultado3',resultados3),
    
]


