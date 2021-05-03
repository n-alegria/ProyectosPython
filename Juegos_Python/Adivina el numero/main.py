#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint

def juego():
    print("""   
    Bienvenido
    
    Se le solicitará que ingrese un numero de cuatro digitos entre el 1000 y 9999 el cual será cotejado con un numero secreto.
    Si el numero ingresado es incorrecto se le volverá a pedir que ingrese un numero nuevamente y se le indicará si el numero secreto
    es mayor o menor al numero que usted ingreso, al finalizar el juego se le indicará la cantidad de intentos que tuvo hasta
    obtener el numero ganador.

    Buena Suerte!""")
    
    numero_secreto = randint(1000, 9999)
    cantidad_intentos = 0
    
    while(True):
        try:
            numero_ingresado = int(input("\nIngrese un numero: "))
            cantidad_intentos += 1
            if(numero_ingresado == numero_secreto):
                print(f"\n->> Ganaste al intento {cantidad_intentos}<<-\n")
                break
            elif(numero_ingresado > numero_secreto):
                print("\n-> El numero que ingresaste es mayor al numero secreto <-")
            elif(numero_ingresado < numero_secreto):
                print("\n-> El numero que ingresaste es menor al numero secreto <-")
            if input('\nContinuar? (s/n): ').lower() != 's':
                break
        except ValueError as e:
            print('\n-> Debe ingresar un numero entero. <-')

if __name__ == '__main__':
    juego()