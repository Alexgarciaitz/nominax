from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import Empleado

def home(request):
    empleados = Empleado.objects.all()
    return render(request, 'home.html' , {'empleados':empleados})
    # return HttpResponse("hola")
# Create your views here.

def eliminar_empleado(request, id):
    empleado =Empleado.objects.get(id=id)
    empleado.delete()
    return redirect('/')
