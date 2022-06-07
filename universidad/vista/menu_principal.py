from modelo.dominio.docente import Docente
from modelo.bd.gestionar_docente import Gestionar_Docente

class Menu_Principal():
    def __init__(self) -> None:
        self.ref_gestionar_docente = Gestionar_Docente()
        self.opciones = ['Estudiante', 'Docente']

    def menu_principal(self):
        print('*'*50)
        print('UNIVERSIDAD')
        print('*'*50)

        indice = 1
        for opcion in self.opciones:
            print('[{}].- {}'.format(indice, opcion))
            indice += 1

        print('[{}].- {}'.format(0, 'Salir'))

    def menu_opcion(self, opcion):
        opcion -= 1

        print('--Gestionar {}--'.format(self.opciones[opcion]))
        print('[1].- Registrar {}'.format(self.opciones[opcion]))
        print('[2].- Modificar {}'.format(self.opciones[opcion]))
        print('[3].- Eliminar {}'.format(self.opciones[opcion]))
        print('[4].- Buscar {}'.format(self.opciones[opcion]))

    def opcion_seleccionada(self, opcion):
        if opcion == 1:
            print('REGISTRAR')
            cedula = input('Cedula: ')
            nombre = input('Nombre: ')
            apellido = input('Apellido: ')
            fecha_ingreso = input('Fecha de Ingreso: ')
            objeto = Docente(cedula, nombre, apellido, fecha_ingreso)
            self.ref_gestionar_docente.insertar(objeto)
        elif opcion == 2:
            print('MODIFICAR')
            cedula = input('Ingresar Cedula para identificar: ')
            nombre = input('Nombre: ')
            apellido = input('Apellido: ')
            fecha_ingreso = input('Fecha de Ingreso: ')

            objeto = Docente(cedula, nombre, apellido, fecha_ingreso)
            self.ref_gestionar_docente.modificar(objeto)
        elif opcion == 3:
            print('ELIMINAR')
            cedula = input('Ingresar Cedula para identificar: ')

            objeto = Docente(cedula, None, None, None)
            self.ref_gestionar_docente.eliminar(objeto)
        elif opcion == 4:
            self.ref_gestionar_docente.leer(None)
