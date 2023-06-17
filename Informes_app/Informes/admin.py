from django.contrib import admin
from .models import Usuario, Regional, Especialidad, Prestador, InformeModificacionUsuarios, AdminContratacion, Rol, Estado, Perfil


admin.site.register(Usuario)
admin.site.register(Regional)
admin.site.register(Especialidad)
admin.site.register(Prestador)
admin.site.register(InformeModificacionUsuarios)
admin.site.register(AdminContratacion)
admin.site.register(Rol)
admin.site.register(Estado)
admin.site.register(Perfil)

# Register your models here.
