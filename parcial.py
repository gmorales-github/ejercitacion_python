#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Declaración de variables
n = int(input("Por favor ingresar el número hasta el cúal desea comprobar: "))
numero = 0
numeros = []
primos = []
noprimos = []

# Declaración de funciones
# Definimos la función para calcular si un número es primo o no
def esprimo(n):
    for i in range(2, n):        
        if n % i == 0:
            return False

    return True        

# Definimos una función para cargar la lista de numeros hasta n
def cargarNumeros(n):
    for i in range(2, n+1):
        numeros.append(i)

# Definimos una función para cargar la lista de numeros primos y no primos
def cargarPrimosNoPrimos(numeros):
    for numero in numeros:
        if esprimo(numero) == True:
            primos.append(numero)
        else:
            noprimos.append(numero)

        numero = numero + 1


# Inicio del código del programa
if n <= 1:
        print("Debe ingresar valores mayores a 2")

else:
    # Cargo la lista numeros hasta n
    cargarNumeros(n)

    # Muestro los números de la lista
    print("Usted desea comprobar si la siguiente lista de números", numeros, "son primos")

    # Cargo la lista de números primos y no primos
    cargarPrimosNoPrimos(numeros)

# Visualizó los primos y no primos
print("Listado de números primos: ", primos)
print("Listado de números no primos: ", noprimos)