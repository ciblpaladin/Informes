from ...models import Usuario
from ...Interfaces.ReadInterface import ReadInterface
from ...Interfaces.WriteInterface import WriteInterface


class UsuariosService(ReadInterface,WriteInterface):

    def all(self):
        return Usuario.objects.all()
    
    def get(self, id):
        pass

    def create(self,model):
        
        Usuario.objects.create(**model)

    def update(self):
        pass

