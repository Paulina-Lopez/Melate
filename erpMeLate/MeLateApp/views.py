from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def inicioDeSesion(request):
    return render(request, 'ingreso.html')

def registro(request):
    return HttpResponse("<html><body>Estas Registrado</body></html>")