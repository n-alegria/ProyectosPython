#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, sys

def juego():
    print("""   
    Bienvenido
    
    Se le solicitará que ingrese un numero de cuatro digitos el cual será cotejado con un numero secreto generado automaticamente.
    Si el numero ingresado es incorrecto se le vovlerá a pedir que ingrese un numero nuevamente y se le indicará si el numero secreto
    es mayor o menor al numero que usted ingreso, al finalizar el juego se le indicará la cantidad de intentos que tuvo hasta
    obtener el numero ganador.

    Buena Suerte!
    """)
    
    # Numero secreto generado con el metodo 'random'
    numeroSecreto = random.randint(1000, 9999)
    cantidadIntentos = 0
    seguir = True

    # --> print(numeroSecreto) # <-- Lo muestro
    
    while(seguir):
        # Solicito el ingreso del numero y sumo 1 a la cantidad de intentos
        numeroIngresado = int(input("Ingrese un numero: "))
        cantidadIntentos += 1
        # En caso de ser correcto lo informo, muestro la cantidad de intentos y modifico el 'seguir' en 'false'
        # para que termine la iteraccion del 'while'
        if(numeroIngresado == numeroSecreto):
            print(f"Ganaste al {cantidadIntentos} intento\n")
            seguir = False
        elif(numeroIngresado > numeroSecreto):
            print("El numero que ingresaste es mayor al numero secreto")
        elif(numeroIngresado < numeroSecreto):
            print("El numero que ingresaste es menor al numero secreto")

juego()