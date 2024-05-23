#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Calcular el promedio de nota obtenido por un alumno, teniendo 7 notas en el año.

# Declaro las variables globales y la lista
valido = True
notas = []

# Declaro las funciones
# Cargo las notas en una lista
def cargarNotas():
    i = 7
        
    while i > 0:
        notas.append(int(input("Ingrese el valor de la nota: ")))
        i = i - 1


# Sumo todas las notas dentro de la lista
def sumarNotas():
    '''Retorna la suma de todos los elementos de una lista '''
    suma = 0
    
    for elemento in notas:
        suma = suma + elemento

    return suma / 7


# Flujo principal del programa
while valido == True:
    try:
        cargarNotas()
        
        # Valido que los elementos de la lista notas sean mayores a 0
        for nota in notas:
            if nota < 0:
                notas = []
                raise ValueError()
        
        valido = False
        print("El promedio de las notas es: ", sumarNotas())
        

    except ValueError:
        print("Por favor ingrese datos númericos válidos")      