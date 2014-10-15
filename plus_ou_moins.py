# -*- coding: latin-1 -*-

from random import randrange

print("-- Jeu du plus ou moins --")

nb_choisi = 0
nb_rand = randrange(500)

while nb_choisi != nb_rand:
	nb_choisi = int(input("Choisissez un nombre : "))

	if nb_choisi < nb_rand:
		print("C'est plus !")
	elif nb_choisi > nb_rand:
		print("C'est moins !")
	elif nb_choisi == nb_rand:
		print("Bravo, vous avez trouvé le nombre !")