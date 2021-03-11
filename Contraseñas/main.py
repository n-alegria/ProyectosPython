from packages.menu import Menu

if __name__ == '__main__':
    while True:
        Menu.mensaje_bienvenida()
        Menu.seleccionar_opcion()
        if Menu._opcion == 1:
            Menu.agregar_contrasenia()
        elif Menu._opcion == 2:
            Menu.eliminar_contrasenia()
        elif Menu._opcion == 3:
            Menu.listar_contrasenias()
        elif Menu._opcion == 4:
            Menu.listar_vencidas()
        elif Menu._opcion == 5:
            print('\n -> Gracias por ingresar <-')
            break
        else:
            print('\n --> Opcion Incorrecta <--')
    
