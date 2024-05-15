# Tipo de triángulo según 3 valores ingresados.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
	try:
		ladoA = int(input("ingrece la medida del lado 1 en cm: "))
		ladoB = int(input("ingrece la medida del lado 2 en cm: "))
		ladoC = int(input("ingrece la medida del lado 3 en cm: "))
	except ValueError:
		print("La medida debe ser un munero mayor a 0")
	else:
		if ladoA <= 0:
			print("La medida 1 no puede ser menor a 0.")
		elif ladoB <= 0:
			print("La medida 2 no puede ser menor a 0.")
		elif ladoC <= 0:
			print("La medida 3 no puede ser menor a 0.")
		else:
			break

if ladoA == ladoB and ladoA == ladoC:
     print("El triagulo es un equilatero")
elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
     print("El triangulo es un isósceles")
else:
     print("el triangulo es un escaleno")