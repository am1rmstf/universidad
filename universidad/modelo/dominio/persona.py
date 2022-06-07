class Persona:
    def __init__(self, cedula, nombre, apellido):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, nuevo_valor):
        self._cedula = nuevo_valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_valor):
        self._nombre = nuevo_valor

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, nuevo_valor):
        self._apellido = nuevo_valor