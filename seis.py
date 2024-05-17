#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escribir un programa que pregunte al usuario por el número de horas trabajadas y
# el costo por hora. Después debe mostrar por pantalla el pago que le corresponde.

# Declaro las variables
valido = True

# Declaro la función calculoHoras()
def calculoHoras():
    valor = horas_trabajadas * costo_hora
    return f" El pago corresponte es: {valor} pesos"


while valido == True:
    try:
        horas_trabajadas = float(input("Ingrese la cantidad total de horas trabajadas: "))
        costo_hora = float(input("Ingrese el costo por horas trabajadas: "))
        print(calculoHoras())
        valido = False

    except ValueError:
        print("Por favor debe ingresar valores númericos.")