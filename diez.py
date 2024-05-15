# Se pide obtener la calificación final de un examen, teniendo un 
# nro de respuesta correctas que suman 4 puntos c/u, 
# un nro de respuestas incorrectas que restan 1 punto por c/u y 
# un nro de respuestas en blanco.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Declaro las variables
valido = True

# Defino la función obtener calificación
def obtCalif():
    '''Función que retorna el valor de la calificación.'''
    if respOk <= 0 or respNoOk <= 0:
        return print("Por favor ingresar un valor mayor que cero.")        
    
    else:
        calif = respOk * 4 - respNoOk
        return calif

while valido == True:
    """Válido si accidentalmente se ingresa un valor que no sea entero."""
    try:
        respOk = int(input("Ingrese la cantidad de respuestas correctas: "))
        respNoOk = int(input("Ingrese la cantidad de respuestas incorrectas: "))        
        
        valido = False        

    except ValueError:
        print("Debe ingresar un valor vaĺido")

# Muestro por consola el valor de la calificación a través de la función obtCalif()
if obtCalif() != None:
    print("El valor de la calificación obtenida es: ", obtCalif())