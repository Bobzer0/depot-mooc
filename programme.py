# -*-coding: latin-1 -*-

operateur = 0

print("-- Calculatrice --\n")

nombre1 = int(input("Entrez le premier nombre : "))
nombre2 = int(input("Entrez le deuxième nombre : "))

while (operateur != 1 and operateur != 2 and operateur != 3 and operateur != 4):
	operateur = int(input("Choisissez l'opération a effectuer :\n1 = addition\n2 = soustraction\n3 = multiplication\n4 = division\n"))

if operateur == 1:
	print(nombre1, '+', nombre2, '=', nombre1 + nombre2)
elif operateur == 2:
	print(nombre1, '-', nombre2, '=', nombre1 - nombre2)
elif operateur == 3:
	print(nombre1, '*', nombre2, '=', nombre1 * nombre2)
else:
	print(nombre1, '/', nombre2, '=', nombre1 / nombre2)