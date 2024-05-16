#Escriba un programa que pida una cantidad de segundos y
#que escriba cuántos minutos y segundos son.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def convertir():
    '''Convierte segundos a minutos'''

    if segundos <= 0:
        return print("Debe ingresar valores positivos mayores a cero.")
    
    else:
        minutos = int(segundos / 60)
        restosegundos = segundos % 60
        return print("Corresponden a", minutos, "minuto/s" " " "y", restosegundos, "segundo/s")

# Capturo datos ingresados por el usuario en la variable segundos
segundos = int(input("Ingrese la cantidad de segundos: "))
# Utilizó la función convertir()
convertir()