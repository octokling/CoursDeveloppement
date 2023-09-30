#Attention c'est exercice n'est pas une bombe ^^

# Écrire une fonction qui affiche la pyramide de Sastantua à l’écran en fonction d’une taille donnée.
# Une pyramide de taille 0 n’affiche rien. La taille de la pyramide est un nombre entier compris entre 0 et 10 passé en argument à la fonction.
etagePyramid = ["", "", "", "", "", "", "", "", "", ""]

def createPyramid(NumEtage):
    numberOfStar = 1
    for e in range(NumEtage):
        for line in range(4):
            if line < 3:
                etagePyramid[e] = ""
                print("")


createPyramid(1)