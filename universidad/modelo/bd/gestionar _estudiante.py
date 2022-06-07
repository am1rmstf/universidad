from controlador.gestionar_objeto import Gestionar_Objeto

class Gestionar_Estudiante(Gestionar_Objeto):
    def __init__(self):
        self.ref_estudiantes = []

    def insertar(self, objeto):
        self.ref_estudiantes.append(objeto)

    def modificar(self, objeto):
        for elemento in self.ref_estudiantes:
            if elemento.cedula == objeto.cedula:
                elemento.nombre = objeto.nombre
                elemento.apellido = objeto.apellido
                elemento.fecha_ingreso = objeto.fecha_ingreso

    def eliminar(self, objeto):
        for elemento in self.ref_estudiantes:
            if elemento.cedula == objeto.cedula:
                self.ref_estudiantes.remove(elemento)

    def leer(self, objeto):
        if objeto is not None:
            for elemento in self.ref_estudiantes:
                if elemento.cedula == objeto.cedula:
                    return elemento
        else:
            for elemento in self.ref_estudiantes:
                print(elemento)
