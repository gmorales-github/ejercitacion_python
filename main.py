#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escribir un programa que permita crear una lista de palabras (que puede ser vacía).
# Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras
# para crear la lista. Por último el programa tiene que mostrar en pantalla la lista creada.

# Importo el módulo palabras (palabras.py)
import palabras as p

# Variables
cant = 0
palabras = []
valido = True

# Inicio del programa
while valido == True:
    try:
        # Ingreso la cantidad total de palabras que voy a cargar
        cant = int(input("Ingresar la cantidad total de palabras para cargar en la lista: "))

        # Valido si el número ingresado de palabras no sea menor a cero
        if cant <= 0:
            print("No puede ingresar valores menores iguales a cero.")
            
            # Vuelve a solicitar que ingrese la cantidad total de palabras
            continue

        else:
             print("A continuación se solicitará ingresar cada una de las palabras a cargar en la lista.")

             cont = 0
             while cont < cant:
                palabra = str(input("Ingrese la palabra: "))
                
                # Valido si es un palabra y el tamañio máximo de 23 carácteres.Cargo la lista de palabras
                if palabra.isalpha() and len(palabra) <= 23 or palabra == "":
                    # Invoco al método cargarPalabra()
                    p.cargarPalabra(palabra, palabras)
                    cont = cont + 1
                
                # En caso de ingresar una palabra invalida vuelvo a iniciar el loop de carga
                else:
                    print("Debe ingresar palabras con letras del abcdario y que no superen más de 23 letras.")
                    print("Recordar: Según la RAE la palabra más extensa del idioma español es: electroencefalografista.")
                    continue              
             
             # Muestro la lista              
             print("La lista es: ", palabras)
             
             
        # Coloco la variable en False para salir del bucle
        valido = False

    except ValueError:
        print("No pueden ser caracteres ni valores decimales. Debe ingresar un valor númerico entero.")