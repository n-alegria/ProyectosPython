#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, sys, os

def juego():
    print("""   
    Bienvenido
    
    Se le solicitará que ingrese un numero de tres digitos el cual será cotejado con un numero secreto generado automaticamente.
    Si el numero ingresado es incorrecto se le vovlerá a pedir que ingrese un numero nuevamente y se le indicará si el numero secreto
    es mayor o menor al numero que usted ingreso.
    En caso de llegar a cinco intentos fallidos se le proporcionara una ayuda, al finalizar el juego se le indicará la cantidad de 
    intentos que tuvo hasta obtener el numero ganador.

    Buena Suerte!
    """)
    
    # Numero secreto generado con el metodo 'random'
    numeroSecreto = random.randint(100, 999)
    cantidadIntentos = 0
    seguir = True

    # --> print(numeroSecreto) # <-- Lo muestro
    
    while(seguir):
        # Solicito el ingreso del numero y sumo 1 a la cantidad de intentos
        numeroIngresado = int(input("Ingrese un numero: "))
        numeroString = (str)(numeroSecreto)
        cantidadIntentos += 1
        # En caso de ser correcto lo informo, muestro la cantidad de intentos y modifico el 'seguir' en 'false'
        # para que termine la iteraccion del 'while'
        if(numeroIngresado == numeroSecreto):
            print(f"--> Ganaste al {cantidadIntentos} intento <--\n")
            seguir = False
        elif(numeroIngresado > numeroSecreto):
            print("\n--> El numero que ingresaste es mayor al numero secreto. <--\n")
        elif(numeroIngresado < numeroSecreto):
            print("\n--> El numero que ingresaste es menor al numero secreto. <--\n")
        if(cantidadIntentos == 3):
            print(f"El primer numero secreto es: {numeroString[0:1]}\n")
        elif(cantidadIntentos == 6):
            print(f"Los primeros dos numeros secretos son: {numeroString[0:2]}\n")

juego()