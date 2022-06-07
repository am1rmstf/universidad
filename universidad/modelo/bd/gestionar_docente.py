from controlador.gestionar_objeto import Gestionar_Objeto

class Gestionar_Docente(Gestionar_Objeto):
    def __init__(self):
        self.ref_docentes = []

    def insertar(self, objeto):
        self.ref_docentes.append(objeto)

    def modificar(self, objeto):
        for elemento in self.ref_docentes:
            if elemento.cedula == objeto.cedula:
                elemento.nombre = objeto.nombre
                elemento.apellido = objeto.apellido
                elemento.fecha_ingreso = objeto.fecha_ingreso

    def eliminar(self, objeto):
        for elemento in self.ref_docentes:
            if elemento.cedula == objeto.cedula:
                self.ref_docentes.remove(elemento)

    def leer(self, objeto):
        if objeto is not None:
            for elemento in self.ref_docentes:
                if elemento.cedula == objeto.cedula:
                    return elemento
        else:
            for elemento in self.ref_docentes:
                print(elemento)
