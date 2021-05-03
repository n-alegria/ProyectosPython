#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint
from exception_number import NumberException

def juego():
    print("""   
    Bienvenido
    
    Se le solicitará que ingrese un numero de tres digitos entre el 100 y 999 el cual será cotejado con un numero secreto generado automaticamente.
    Si el numero ingresado es incorrecto se le vovlerá a pedir que ingrese un numero nuevamente y se le indicará si el numero secreto
    es mayor o menor al numero que usted ingreso.
    En caso de llegar a cinco intentos fallidos se le proporcionara una ayuda, al finalizar el juego se le indicará la cantidad de 
    intentos que tuvo hasta obtener el numero ganador.

    Buena Suerte!""")
    
    numero_secreto = randint(100, 999)
    cantidad_intentos = 0
    continuar = 's'

    while(True):
        try:
            numero_string = input("\nIngrese un numero: ")
            if not numero_string.isnumeric():
                raise NumberException()
            numero_int = int(numero_string)
            cantidad_intentos += 1
            if(numero_int == numero_secreto):
                print(f"\n->> Ganaste al {cantidad_intentos} intento <<-\n")
                break
            elif(numero_int > numero_secreto):
                print("\n--> El numero que ingresaste es mayor al numero secreto <--")
            elif(numero_int < numero_secreto):
                print("\n--> El numero que ingresaste es menor al numero secreto <--")
            if(cantidad_intentos == 4):
                continuar = input('\nContinuar? (s/n): ')
                print(f"\nEl primer numero secreto es: {numero_string[:1]}")
            elif(cantidad_intentos == 8):
                print(f"\nLos primeros dos numeros secretos son: {numero_string[:2]}")
                continuar = input('\nContinuar? (s/n): ')
            if continuar.lower() != 's':
                break
        except NumberException as e:
            print(f'\n-> {e} <-')

if __name__ == '__main__':
    juego()