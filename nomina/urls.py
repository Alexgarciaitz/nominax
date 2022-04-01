from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('eliminar_empleado/<int:id>', views.eliminar_empleado, name='eliminar_empleado'),
    #path('editar_empleado/<int:id>', views.editar_empleado, name='editar_empleado'),
]
