################################################
# title - Hello World python		       #
# date  - 04/09/2017                           #
################################################



############### function #######################



############### body ###########################
import random
r = random.randint(0,3)


mot = ["maison","arbre","informatique","bonbon"]
mot_random=mot[r]
liste_mot_random = list(mot_random)
print mot_random

nbr_lettre = 0
for a in mot_random:
	nbr_lettre = nbr_lettre + 1
	
cache=[1]*nbr_lettre

i = 0
while i < nbr_lettre:
	cache[i] = "_"
	i = i + 1

print cache

tentatives = 0

while tentatives < 7:
	lettre = raw_input("Donnez une lettre :")
	j = 0
	while j < nbr_lettre:
		if mot_random[j]==lettre:
			cache[j]=lettre
			print cache
		else:
			cache[j]="_"
		j = j + 1

	tentatives = tentatives + 1




