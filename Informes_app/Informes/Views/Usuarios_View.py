from typing import Any
from django.views import View
from django.shortcuts import render, redirect
from ..Servicios.Usuarios.UsuariosService import UsuariosService
from ..Servicios.Rol.RolService import RolService
from ..Servicios.Estado.EstadoService import EstadoService
from..Decoradores.ValidateMethod import transform_post_data_to_model

class UsuariosView(View):
    
    def __init__(self, *args, **kwargs):

        self.user_services = UsuariosService()
        
        
    def get(self, request):
        
        usuarios = list(self.user_services.all())
        
        return render(request, "Usuarios/Listado.html", {"usuarios": usuarios})
    
class UsuariosCrear(View):

    def __init__(self):

        self.user_services = UsuariosService()
        self.rol = RolService()
        self.estado = EstadoService()

    def get(self, request):

        roles = self.rol.all()
        estados = self.estado.all()
        return render(request, "Usuarios/Crear.html",{"roles": roles,"estados": estados})     
    
    @transform_post_data_to_model
    def post(self,request):

        self.user_services.create(request.usuario)
        print(request.usuario)
        
        return redirect("usuarios")
      

