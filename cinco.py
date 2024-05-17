#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escriba un programa que pida una temperatura en grados Celsius y que escriba
# esa temperatura en grados Fahrenheit. Se recuerda que la relación entre grados 
# Celsius (C) y grados Fahrenheit (F) es la siguiente: F = 1,8 * C + 32

# Declaro variables
valido = True

# Declaro la función convertirGrados()
def convertirGrados(grados):
    """Convierto los grados °C en °F"""
    f = 1.8 * grados_Celsius + 32
    return f"Son: {f}°F"

# Flujo principal del programa
while valido == True:
    try:
        grados_Celsius = float(input("Ingrese el valor de la temperatura en gardos celsius: "))
        print(convertirGrados(grados = grados_Celsius))        
        valido = False
    
    except ValueError:
        print("Debe ingresar un valor númerico, por favor")