from ...Interfaces.ReadInterface import ReadInterface
from ...models import Rol

class RolService(ReadInterface):

    def all(self):
        
        return Rol.objects.all()

    def get(self, id):

        return Rol.objects.get(id = id)