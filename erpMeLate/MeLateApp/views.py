from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def inicioDeSesion(request):
    return render(request, 'ingreso.html')

def inicio(request):
    return render(request, 'Inicio.html')

def ventas(request):
    return render(request, 'ventas.html')

def insumos(request):
    return render(request, 'insumos.html')

def productos(request):
    return render(request, 'productos.html')

def proveedores(request):
    return render(request, 'proveedores.html')

def registro(request):
    return HttpResponse("<html><body>Estas Registrado</body></html>")