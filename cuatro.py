#Escriba un programa que pida una distancia en pies o pulgadas y que
#escriba esa distancia en centímetros. 
#Se recuerda que un pie son doce pulgadas y una pulgada son 2,54 cm

# Declaro la variable distancia
distancia = 0

print("--- Inicio del programa ---")
# Opciones
opcion = int(input("Elija 1 para pies o 2 para pulgadas."))
if opcion == 1 or opcion == 2:
    distancia = int(input(("Ingrese el valor de la distancia.")))
    
    if distancia <= 0:
        print("Por favor ingrese un valor positivo mayor a cero.")

    else:
        if opcion == 1:
            result =  distancia * 30.48
            print("Los ", distancia, "pies", "son", result, "cm.")
        
        else:
            result = distancia * 2.54
            print("Las ", distancia, "pulgadas", "son", result, "cm.")
    

else:
    print("Por favor ingresar una opción correcta.")    

print("--- Fin del programa ---")