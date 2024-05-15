#Escriba un programa que pida una cantidad de segundos y
#que escriba cuántos minutos y segundos son.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

segundos = int(input("Ingrese la cantidad de segundos: "))

# Convertir segundos a minutos
minutos = int(segundos / 60)
restosegundos = segundos % 60
print("Corresponden a", minutos, "minuto/s" " " "y", restosegundos, "segundo/s")

