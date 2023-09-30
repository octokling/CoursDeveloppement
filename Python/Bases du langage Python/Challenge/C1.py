# Réunir les 2 procédures aff_alpha et aff_rev_alpha de l’exercice 4 en une seule fonction qui revoie une chaîne de caractères contenant l’alphabet. 
# Le sens croissant ou décroissant sera présélectionné par un argument de type chaîne passé à la fonction ‘c’ ou ‘d’.

# En gros on fusionne la fonction aff_alpha() et aff_rev_alpha(), et lorsque l'on va faire aff_alpha(), ou peut choisir dans la fonction soit "c" soit "d" pour les faire afficher soit dans le sens croissant, soit décroissant.

def aff_chif(choix): #C'est une variable que l'on attribue à l'intérieur des () lorsque l'on appele une fonction
    if choix == "c":
        for lettre in range(ord('a'), ord('z') + 1):
            print(chr(lettre), end='')
    elif choix == "d":
        for lettre in range(ord('z'), ord('a') - 1, -1):
            print(chr(lettre), end='')


aff_chif("d") #Je chois l'ordre croissant