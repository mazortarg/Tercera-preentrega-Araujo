from django import forms

class libroFormulario(forms.Form):
    
    titulo = forms.CharField()
    autor = forms.CharField()
    editorial = forms.CharField()
    inventario = forms.IntegerField()
    
class usuarioFormulario(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    Ingreso = forms.IntegerField()
    documento = forms.IntegerField()    
    
class cargarPrestamo(forms.Form):
    inventario = forms.IntegerField()
    documento = forms.IntegerField()
    fecha = forms.DateField()
  
class cargarDevolucion(forms.Form):
    Inventario = forms.IntegerField()
    devolucion = forms.DateField()    