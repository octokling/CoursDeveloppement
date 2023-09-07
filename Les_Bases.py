#Faire des maths 
1+1 #Addition
3-2 #Soustraction
5*10 #Multiplicatoon
4/2 #Divisition
2e10 #Puissance (2 puissance 10)

#Utiliser le module math 
import math #Importer un module
math.sqrt(9) #La racine carré d'un nombre

#Afficher <<Bonjour tout le monde>>
print("Bonjour tout le monde") #Affiche Bonjour tout le monde sur l'écran

#Le programme demandera votre nom, pour ensuite vous le redire.
input("Quel est ton nom ?") #Affiche Quel est ton mot, mais le programme attends une réponse entré par l'utilisateur.

#Le programme demandera votre age, et vous dira votre age.
variable = input("Quel est ton âge ?") #Stocker input dans une variable
print("Tu as", variable, "ans") #Affiche Tu as (valeur de la variable) ans

#Variante 
variable1 = input("Quel est ton âge ?")
print(f"Tu as {variable1} ans")

#Information importante  !!!
# Les variables ont plusieurs types 
# str (String) = Une chaine de caractère 
    # Exemple : Bonjour tout le monde

# int (Integer) = Un nombre entier 
    # Exemple : 360

# float = Un nombre décimal 
    # Exemple : 23,56

# bool (Boolean) = Un variable à deux statistique (Soit true vrai/1 ou false faux/0)
    # Exemple : if 1 + 1 == 3: (1 + 1 n'est pas égale à 1 alors c'est false)