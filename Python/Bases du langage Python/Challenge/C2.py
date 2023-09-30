# Reprendre le prg. construit à l'exercice 5 en y intégrant

# •  L’usage d’une fonction (issue d’un module à importer) qui renvoie l’année actuelle de l’horloge de l’ordinateur.
# •  Un complément pour qu'il affiche si le sujet est majeur ou mineur. Dans ce dernier cas, il affichera aussi l'année de la majorité du sujet.

import datetime #On importe un module qui gère le temps

anneeActuelle = datetime.date.today().year #Nous récupérons avec la librairie datetime, l'année d'aujourd'hui

anneeAge = int(input("Qu'elle est votre année de naissance : "))

if anneeAge >= (anneeActuelle-120) and anneeAge <= anneeActuelle :
    age = anneeActuelle - anneeAge

    print("Vous avez", age ,"ans,", end=" ")
    if age <= 17:
        print("et vous êtes mineur. Vous aurez 18 ans dans", 18 - age, "ans. En", anneeAge + (18 - age))
    else:
        print("et vous êtes majeur. Cela fait", age - 18, "ans que vous êtes majeur. En", anneeAge + 18)
else:
    print("Alors en faite, tu es un esprit ?!? 💀💀💀💀💀💀")