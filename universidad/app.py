from vista.menu_principal import Menu_Principal

if __name__ == '__main__':
    app = Menu_Principal()

    while(True):
        app.menu_principal()
        opcion = int(input('Ingresar opcion: '))

        if opcion == 0:
            break

        app.menu_opcion(opcion)
        opcion = int(input('Ingresar opcion: '))
        app.opcion_seleccionada(opcion)
