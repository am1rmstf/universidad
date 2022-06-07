from abc import ABC, abstractmethod

class Gestionar_Objeto(ABC):
    @abstractmethod
    def insertar(self, objeto):
        pass

    @abstractmethod
    def modificar(self, objeto):
        pass

    @abstractmethod
    def eliminar(self, objeto):
        pass

    @abstractmethod
    def leer(self, objeto):
        pass
    