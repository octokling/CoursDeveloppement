#Écrire un programme qui demande à l'utilisateur son année de naissance et qui affiche son âge. 
#Indication : L'année courante sera mise dans une variable (immuable) initialisée en début de prg.

anneeActuelle = 2023 #Nous déclarons l'année actuelle comme dans l'indice

anneeAge = input("Qu'elle est votre année de naissance")#Nous faisons un input pour récup l'année de naissance du l'utilisateur

print("Vous avez", anneeActuelle - int(anneeAge),"ans") #Nous faisons un print avec anneeActuelle - anneeAge(converti en int) pour savoir l'age.
#Très simple et très efficasse

#BONUS faire exactement le même code mais en allant chercher l'année automatiquement

import datetime #On importe un module qui gère le temps

anneeActuelle2 = datetime.date.today().year #Nous récupérons avec la librairie datetime, l'année d'aujourd'hui

anneeAge2 = input("Qu'elle est votre année de naissance")

print("Vous avez", anneeActuelle2 - anneeAge2,"ans") #Et nous printons ^^

#And that it !!!