#!/usr/bin/python3
from packages.conexion_api import *
from packages.funcion_main import *

if __name__ == '__main__':
    listado_pokemon = []
    while True:
        mensaje_bienvenida()
        opcion = seleccionar_opcion('Ingrese una opcion')

        if opcion == '1':
            buscar_pkm(listado_pokemon)
        elif opcion == '2':
            listar_pokemon(listado_pokemon)
        elif opcion == '5':
            despedida()
            break
        else:
            ingreso_incorrecto()