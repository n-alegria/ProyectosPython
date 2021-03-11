#!/usr/bin/python3
from packages.conexion_api import *
from packages.pokemon import Pokemon
import os

def mensaje_bienvenida():
    """
    Brinda un mensaje con un menu de opciones.
    """
    clear()
    print('''    Bienvenido.

        1) Pokemon por nombre o ID.
        2) Listar Pokemon.

        5) Salir.
        ''')

def seleccionar_opcion(mensaje:str):
    """
    Retorna un 'string' el cual servira como seleccion para las opciones.
    """
    return input(f'\n{mensaje}: ')

def buscar_pkm(lista:list):
    clear()
    print(f'--> Busqueda de pokemon por nombre o id')
    pokemon = busqueda_pkm(seleccionar_opcion(f'Ingrese el nombre/id del pokemon'))
    if pokemon != None:
        print(f'''
        Name: {pokemon['name'].capitalize()}
        ID: {pokemon['id']}
        Height: {pokemon['height']}
        Weight: {pokemon['weight']}
        ''')
        
        confirmacion = input('¿Desea capturar al pokemon? (s/n): ')
        if pokemon in lista:
            print('\n--> El pokemon ya se encuentra en la pokedex. <--')
        else:
            if confirmacion.lower() == 's':
                nombre_pkm = pokemon['name']
                nombre_pkm = Pokemon(pokemon)
                lista.append(nombre_pkm)
                print('\n--> Se ha capturado al pokemon. <--')
            else:
                print('\n--> No se ha capturado al pokemon. <--')

        print('\n--> Ingrese una tecla para continuar...', end='')
        input()
    else:
        print(f'\n--> No existe Pokemon con ese nombre/id. <--')


def listar_pokemon(lista:list):
    """
    Lista todos los pokemon capturados.
    """
    clear()
    if len(lista) > 0:
        print(f'--> Pokemon capturados.\n')
        print(f"{'ID'.rjust(15, ' ')}  |  {'Nombre'.ljust(15, ' ')}")
        for pk in lista:
            print(f"{pk.id:15}  |  {pk.nombre.capitalize():15}")
    else:
        print('--> La lista esta vacia.\n')
    print('\n--> Ingrese una tecla para continuar...', end='')
    input()

def despedida():
    """
    Limpia la pantalla luego da unmensaje de despedida y cierra el programa.
    """
    clear()
    print('--> Gracias por elegirnos <--')

def ingreso_incorrecto():
    """
    Mensaje en caso de ingresar una opcion incorrecta.
    """
    clear()
    print('--> Opcion incorrecta. Reintente\n')
    print('--> Ingrese una tecla para continuar...', end='')
    input()

def clear():
    """
    Limpia la pantalla.
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")