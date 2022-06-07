from modelo.dominio.persona import Persona

class Estudiante(Persona):
    def __init__(self, cedula, nombre, apellido, fecha_nacimiento):
        super().__init__(cedula, nombre, apellido)
        self.__fecha_nacimiento = fecha_nacimiento

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, nuevo_valor):
        self.__fecha_nacimiento = nuevo_valor

    def __str__(self):
        return self.cedula + ' : ' + self.nombre + ' - ' + self.apellido