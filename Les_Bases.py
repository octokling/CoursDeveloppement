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

# bool (Boolean) = Un variable à deux statistique (Soit True vrai/1 ou False faux/0)
    # Exemple : 1 + 1 == 3 (1 + 1 n'est pas égale à 3 alors c'est False)


# Les conditions 
vrai = True #Ceci est une variable boolean de condition Vrai
faux = False #Ceci est une variable boolean de condition Faux

estVrai = 1 + 1 == 2 #Nous pouvons aussi déclarer une boolean en faisant une vérification. Par exemple, cette variable sera vrai car 1+1 est bien égale à 2 (les == veux dire est égale à)
estFaux = 2 * 2 == 6 #Déclare aussi une boolean en faisant une vérification. Par exemple, cette variable sera fausse car 2x2 est pas égale à 6 

if estVrai: #Ceci est une conditions, if = si, si l'information est vrai/True, alors il l'execute le code à l'intérieur de la condition
    print("C'est vrai")
else: #Ceci est un else/sinon. Si la condition d'avant était fausse, alors on éxecute cette partie de code. Il n'est pas obligatoire de le mettre après un if
    print("C'est faux")

if estFaux:
    print("C'est vrai")
else:
    print("C'est faux")