
from django.shortcuts import render
from ..models import Usuario, Rol, Estado

def transform_post_data_to_model(func):
    def wrapper( *args, **kwargs):
        
        request = args[1]
        usuarios = {}

        foreings_key = {
            "rol_fk" : lambda id: Rol.objects.get(id=id),
            "estado_usuario" : lambda id: Estado.objects.get(id=id)
        }

        if request.method == "POST":
            for key, valor in request.POST.items():

                if key != "csrfmiddlewaretoken":
                    if key in foreings_key:
                        usuarios[key] = foreings_key[key](valor)
                    else:
                        usuarios[key] = valor

        request.usuario = usuarios   

        return func(*args, **kwargs)

    return wrapper