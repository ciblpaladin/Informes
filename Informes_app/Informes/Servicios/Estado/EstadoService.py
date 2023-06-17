from ...Interfaces.ReadInterface import ReadInterface
from ...models import Estado

class EstadoService(ReadInterface):

    def all(self):
        
        return Estado.objects.all()

    def get(self, id):
        
        pass

