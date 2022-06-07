from modelo.dominio.persona import Persona

class Docente(Persona):
    def __init__(self, cedula, nombre, apellido, fecha_ingreso):
        super().__init__(cedula, nombre, apellido)
        self.__fecha_ingreso = fecha_ingreso

    @property
    def fecha_ingreso(self):
        return self.__fecha_ingreso

    @fecha_ingreso.setter
    def fecha_ingreso(self, nuevo_valor):
        self.__fecha_ingreso = nuevo_valor

    def __str__(self):
        return self.cedula + ' : ' + self.nombre + ' - ' + self.apellido