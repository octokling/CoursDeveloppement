#Nous allons développer un TicTacToe jouable sur CMD 

import os #Je ne sais pas trop ce que c'est cette librairie, mais elle permet de modifier le cmd

liste = [" ", " ", " ", " ", " ", " ", " ", " ", " "] #Ceci est une liste, à laquelle plusieurs valeur peuvent être stocker dans une variable
#Liste est actuellement le jeu.
placement = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
#Placement est le nom des emplacement du jeu
isPlayerOneTurn = True #Boolean qui sert à savoir si c'est au joueur 1 de jouer

def isNotAlreadyPlayed(TableId): #Ceci est une fonction, ici on veux importer une variable et cette variable va s'appeler TableId
    #Elle est utilisé pour voir si dans liste la valeur sélectionné à déjà été modifié ou pas
    if not (liste[TableId] == "X" or liste[TableId] == "O"): # not est l'inverse de la réponse. Exemple not True = False
        #Cette condition est exécuté lorsque dans liste et la valeur sélectionné n'est pas égale à X ou à O 
        if isPlayerOneTurn == True: # Si c'est au tour du joueur 1
            liste[TableId] = "X" #Changer dans liste une valeur sélectionné par X
            return True # Retourne Vrai
        else: #Sinon 
            liste[TableId] = "O" #Changer dans liste une valeur sélectionné par O
            return True # Retourne Vrai également
    else:
        return False# Retourne faux
            
def isPlayerOneWin(): #Une fonction pour savoir si player 1 à gagné
    #Toutes les combinaisons possible pour gagné, je vous laisse déchiffré :)
    if liste[0] == "X" and liste[1] == "X" and liste[2] == "X":
        return True
    elif liste[3] == "X" and liste[4] == "X" and liste[5] == "X":
        return True
    elif liste[6] == "X" and liste[7] == "X" and liste[8] == "X":
        return True
    elif liste[0] == "X" and liste[3] == "X" and liste[6] == "X":
        return True
    elif liste[1] == "X" and liste[4] == "X" and liste[7] == "X":
        return True
    elif liste[2] == "X" and liste[5] == "X" and liste[8] == "X":
        return True
    elif liste[0] == "X" and liste[4] == "X" and liste[8] == "X":
        return True
    elif liste[2] == "X" and liste[4] == "X" and liste[6] == "X":
        return True
    else: 
        return False
    
def isPlayerTwoWin():#Pareil mais pour le joueur 2
    if liste[0] == "O" and liste[1] == "O" and liste[2] == "O":
        return True
    elif liste[3] == "O" and liste[4] == "O" and liste[5] == "O":
        return True
    elif liste[6] == "O" and liste[7] == "O" and liste[8] == "O":
        return True
    elif liste[0] == "O" and liste[3] == "O" and liste[6] == "O":
        return True
    elif liste[1] == "O" and liste[4] == "O" and liste[7] == "O":
        return True
    elif liste[2] == "O" and liste[5] == "O" and liste[8] == "O":
        return True
    elif liste[0] == "O" and liste[4] == "O" and liste[8] == "O":
        return True
    elif liste[2] == "O" and liste[4] == "O" and liste[6] == "O":
        return True
    else: 
        return False
    
def nullGame(): #Fonction pour savoir si le jeu est nulle
    if liste[0] != " " and  liste[1] != " " and  liste[2] != " " and  liste[3] != " " and  liste[4] != " " and  liste[5] != " " and  liste[6] != " " and  liste[7] != " " and  liste[8] != " ": #Lorsque tout la liste ne possède plus de caractère invisible
        return True
    else:
        return False


while(True): #Boucle infini jusqu'à un break
    os.system("cls") #Efface l'historique d'écriture dans un CMD
    correctlySelectPlacement = False #Boolean value pour savoir si le joueur à correctement sélectionné un emplacement
    print(f" {liste[0]}|{liste[1]}|{liste[2]}\n-------\n {liste[3]}|{liste[4]}|{liste[5]}\n-------\n {liste[6]}|{liste[7]}|{liste[8]}")#Ecriture de la grille
    
    if isPlayerOneWin(): #Si la fonction retourne vrai
        print("Joueux X à gagné !")
        break
    elif isPlayerTwoWin(): #Si la fonction retourne vrai
        print("Joueur O à gagné !")
        break
    elif nullGame(): #Ta compris j'espère ?...
        print("Partie nulle !")
        break


    while(not correctlySelectPlacement):#Boucle jusqu'à ce que correctlySelectPlacement est égale à False
        PlacementId = 0 #Savoir l'id de l'emplacement en fonction de liste et placement
            
        if isPlayerOneTurn:#Si vraie
            playerChoice = str(input("Placement de votre X : ")) #Convertir en string l'emplacement
            for curPlacement in placement: #curPlacement va avoir un par un les valeurs de placement
                #Par exemple maListe = ["Un", "Deux", Trois]
                #Il y aura trois boucle et curPlacement commencera la première boucle avec la valeur Un, puis deuxième avec Deux puis la troisième par Trois. Capiche ?
                if curPlacement.lower() == playerChoice.lower(): #.lower() mettre tout en minuscule si possible
                    correctlySelectPlacement = isNotAlreadyPlayed(PlacementId) #correctlySelectPlacement égale au retournement de la fonction
                    if correctlySelectPlacement == True: #Si vraie
                        isPlayerOneTurn = False #Set to False (Oui j'adore l'anglais :D)
                    break #Arrête de force la boucle
                else:
                    PlacementId = PlacementId + 1 #Ajout de 1 à PlacementId
        else:
            #Et après c'est la même chose ^^
            playerChoice = str(input("Placement de votre O : "))
            for curPlacement in placement:
                if curPlacement.lower() == playerChoice.lower():
                    correctlySelectPlacement = isNotAlreadyPlayed(PlacementId)
                    if correctlySelectPlacement == True:
                        isPlayerOneTurn = True
                    break
                else:
                    PlacementId = PlacementId + 1

#Si tu n'as pas vraiment compris qu'est ce que je viens de faire, tu peux me solliciter à tout moment ^^