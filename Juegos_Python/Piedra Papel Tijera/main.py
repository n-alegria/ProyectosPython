#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# Solicito los nombres de los jugadores
usuarioUno = input("Nombre primer jugador: ")
usuarioDos = input("Nombre segundo jugador: ")

# Solicito sus respuestas y las casteo a minusculas
respuestaUno = input(f"\n{usuarioUno}, Elija: piedra, papel o tijera: ").lower()
respuestaDos = input(f"{usuarioDos}, Elija: piedra, papel o tijera: ").lower()

def juego(unoRespuesta, dosRespuesta):
    if unoRespuesta == dosRespuesta:
        return("\nEs un empate!")
    elif unoRespuesta == "piedra":
        if dosRespuesta == "tijera":
            return(f"\n{usuarioUno} gana!\n")
        else:
            return(f"\n{usuarioDos} gana!\n")
    elif unoRespuesta == "tijera":
        if dosRespuesta == 'papel':
            return(f"\n{usuarioUno} gana!\n")
        else:
            return(f"\n{usuarioDos} gana!\n")
    elif unoRespuesta == "papel":
        if(dosRespuesta == "piedra"):
            return(f"\n{usuarioUno} gana!\n")
        else:
            return(f"\n{usuarioDos} gana!\n")
    else:
        return("Ingreso invalido, intente nuevamente!")
        sys.exit()

print(juego(respuestaUno, respuestaDos))