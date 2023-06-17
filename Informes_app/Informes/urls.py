from django.urls import path
from .Views import Main
from .Views.Usuarios_View import UsuariosView, UsuariosCrear
from .Views.Informes import Informes

urlpatterns = [

    path('main', Main.Main),
    path('usuario/usuarios', UsuariosView.as_view(), name='usuarios'),
    path('usuario/crear', UsuariosCrear.as_view(), name='crear_usuario'),
    path('informe/informes', Informes.get)

]