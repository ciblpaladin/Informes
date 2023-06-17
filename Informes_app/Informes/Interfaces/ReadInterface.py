from abc import ABC, abstractmethod

class ReadInterface(ABC):
    
    @abstractmethod
    def all():
        pass

    @abstractmethod    
    def get(self, id):
        pass