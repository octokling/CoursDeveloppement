#Affichage de caractères

#Écrire une procédure aff_chif() qui affiche tous les chiffres sur une seule ligne, dans l’ordre croissant.

#Cela veut dire grosso merdo qu'il faut créer une fonction.
#Cette fonction aura pour but d'envoyer d'une traite et d'une seule ligne tout les chiffre dans l'ordre croissant

#J'avais prévu de le faire d'une manière logique qui est de faire une boucle

def aff_chif(): # def = define, on a donc défini une fonction avec pour nom aff_chif. Le symbole : est à mettre car ça déclare le début de la fonction.
    for chiffre in range(10): # for = pour atteindre, range = ranger de 0 à 9 (comme un compteur). En gros ce bout de code génére une boucle jusqu'à ce que range ai terminé de compter
        # chiffre est une déclaration de variable après le for, et range lui attribue donc son avancement dans son comptage.
        print(chiffre, end='') # Et on affiche le résultat. end='' défini qu'après avoir affiché la variable ce qu'il doit écrire à la fin. 
        # par défaut il fait un saut de ligne, le laissé vide lui annulera donc son saut de ligne
        # Si j'aurais remplacé end='' par end='_-A', j'aurais eu ceci sur python : 0_-A1_-A2_-A3_-A4_-A5_-A6_-A7_-A8_-A9_-A

aff_chif() # On appele la fonction créé précédement, la fonction ne s'éxécutera jamais si on ne l'appelle pas !

print()#Fait un saut de ligne

#Écrire une procédure aff_alpha() qui affiche l’alphabet en minuscule sur une seule ligne, dans l’ordre croissant, à partir de la lettre ’a’.
#Bon...
#Maintenant pareil, mais pour l'alphabet...

def aff_alpha(): #On défini une seconde fois une fonction, tu connais ;)
    for lettre in range(ord('a'), ord('z') + 1): # C'est pareil qu'avant pour for et lettre , sauf pour range. ord() permet d'obtenir en int la valeur ASCII d'une lettre.
        # La lettre a minuscule est égale à 97 et la lettre z minuscule à 122, donc avec range, on lui dit de compter de 97 à 122
        #On a rajouter un + 1 car la fonction range compte à partir de 0, donc s'arrêtera à 122, donc z ne serais pas affiché.
        
        #Voici un exemple :
        #range(15) -> ce que l'on obtiens : 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14, avec le zéro, il aura écrit 15 chiffre.
        #Donc pour 122 - 97 = 25, range(ord('a'), ord('z')) -> ce que l'on obtiens : a b c d e f g h i j k l m n o p q r s t u v w x y. soit 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
        
        #Je ne sais pas si c'est clair mais vas-y si vous avez r compris adressez-vous à moi car c'est assez important et récurrent dans la programmation, demandez moi !!!!

        print(chr(lettre), end='') # Et on affiche le résultat avec end un anti saut de ligne. chr() permet de convertir une valeur int en un caractère ASCII.
        #Par exemple chr(97), cela me donne a. chr(110), cela me donne n

aff_alpha() #La team, on oublie à d'appeler la function et de revenir tout à gauche de la ligne, sinon c'est compté comme dans la fonction bg ;)
#LES ESPACEMENTS SONT IMPORTANT ICI !!!!

#Ducoup si tu as compris ça, déjà GG 👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏
#Et donc tu est maintenant capable de faire le dernier tout seul

print()#Fait un saut de ligne

#Écrire une procédure aff_rev_alpha() qui affiche l’alphabet en minuscule sur une seule ligne, dans l’ordre décroissant, à partir de la lettre ’z’.

#🅒🅞🅡🅡🅔🅒🅣🅘🅞🅝 🅛🅘🅖🅝🅔 ❶⓿⓿

#Ensuite je ne sais pas ce qu'est le challange C1 et en vrai OSEF non ?
















































def aff_rev_alpha(): #Aller ! C'est la fête on en déclare un dernière ^^
    for lettre in range(ord('z'), ord('a') - 1, -1): #On inverse ord, on fait -1 pour la règle de compter à partir de 0 (mais à l'envers aussi) oui le -1 après la virgule signie à dire à range() qu'il doit compter de -1 en -1 (On peut égalemenet lui faire compté tout les 2, -2, 5, 100, -1000 etc...)
        #Mais la on à mit -1 car on compte en décroissant : 9 8 7 6 5 4 3 2 1 0
        print(chr(lettre), end='') #EL FAMOSO print with chr convertitor 

aff_rev_alpha() #Puis comme d'hab bg ;)