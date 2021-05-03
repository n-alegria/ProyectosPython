#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    print("""   
Bienvenido
    
    Juego de Piedra, Papel o Tijeras entre dos jugadores, gana el mejor de 3.
    Buena Suerte!
    """)
    
    primer_jugador = input("Nombre primer jugador: ").capitalize()
    segundo_jugador = input("Nombre segundo jugador: ").capitalize()

    ganadas_primero = 0
    ganadas_segundo = 0
    
    while True:
        respuesta_primero = input(f"\n{primer_jugador}, Elija: piedra, papel o tijera: ").lower()
        respuesta_segundo = input(f"{segundo_jugador}, Elija: piedra, papel o tijera: ").lower()
        
        if respuesta_primero == respuesta_segundo:
            print("\nEs un empate!")
        elif respuesta_primero == "piedra":
            if respuesta_segundo == "tijera":
                ganadas_primero += 1
                print(f"\n{primer_jugador} gana!")
            else:
                ganadas_segundo += 1
                print(f"\n{segundo_jugador} gana!")
        elif respuesta_primero == "tijera":
            if respuesta_segundo == 'papel':
                ganadas_primero += 1
                print(f"\n{primer_jugador} gana!")
            else:
                ganadas_segundo += 1
                print(f"\n{segundo_jugador} gana!")
        elif respuesta_primero == "papel":
            if(respuesta_segundo == "piedra"):
                ganadas_primero += 1
                print(f"\n{primer_jugador} gana!")
            else:
                ganadas_segundo += 1
                print(f"\n{segundo_jugador} gana!")
        else:
            print("Ingreso invalido, intente nuevamente!")
        if ganadas_primero == 3 or ganadas_segundo == 3:
            if ganadas_primero == 3:
                print(f'\n->> {primer_jugador} es el ganador! <<-')
            else:
                print(f'\n->> {segundo_jugador} es el ganador! <<-')
            break