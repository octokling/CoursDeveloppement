#Nous allons développer un TicTacToe jouable sur CMD 

import os
liste = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
placement = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
isPlayerOneTurn = True

def isNotAlreadyPlayed(TableId):
    if not (liste[TableId] == "X" or liste[TableId] == "O"):
        if isPlayerOneTurn == True:
            liste[TableId] = "X"
            return True
        else:
            liste[TableId] = "O"
            return True
    else:
        return False
        
def isPlayerOneWin():
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
    
def isPlayerTwoWin():
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


while(True):
    os.system("cls")
    correctlySelectPlacement = False
    print(f" {liste[0]}|{liste[1]}|{liste[2]}\n-------\n {liste[3]}|{liste[4]}|{liste[5]}\n-------\n {liste[6]}|{liste[7]}|{liste[8]}")
    
    if isPlayerOneWin():
        print("Joueux X à gagné !")
        break
    elif isPlayerTwoWin():
        print("Joueur O à gagné !")
        break

    while(not correctlySelectPlacement):
        PlacementId = 0 
            
        if isPlayerOneTurn:
            playerChoice = str(input("Placement de votre X : "))
            for curPlacement in placement:
                if curPlacement.lower() == playerChoice.lower():
                    correctlySelectPlacement = isNotAlreadyPlayed(PlacementId)
                    if correctlySelectPlacement == True:
                        isPlayerOneTurn = False
                    break
                else:
                    PlacementId = PlacementId + 1
        else:
            playerChoice = str(input("Placement de votre O : "))
            for curPlacement in placement:
                if curPlacement.lower() == playerChoice.lower():
                    correctlySelectPlacement = isNotAlreadyPlayed(PlacementId)
                    if correctlySelectPlacement == True:
                        isPlayerOneTurn = True
                    break
                else:
                    PlacementId = PlacementId + 1