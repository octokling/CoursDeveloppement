#Écrire un algorithme permettant d'afficher la tarification d'une lettre à partir de son poids saisi par l'utilisateur.
#1. Poids < 20g : 0,53 €
#2. Poids ≥ 20g et ≤ 50g : 0,70€
#3. Poids > 50g : 1,10€


try: #Essaie (En gros il va essayer de faire le code, et dès qu'une erreur se produit, il peut la capturer)
    poidsLettre = float(input("Saisissez votre poids de votre lettre en Gramme")) #Converti en float input

    if poidsLettre <= 0: raise ValueError() #Je génère une erreur de type ValueError lorsque la lettre fait un poids de 0 ou moins

    prix = 0.0 #Déclare prix
    if poidsLettre < 20 : #Si poidsLettre est plus petit que 20
        prix = 0.53 #Redéfinir la valeur de prix
    elif poidsLettre >= 20 and poidsLettre <= 50: #Sinon si poidsLettre entre 20 et 50
        prix = 0.70 #Redéfinir la valeur de prix
    elif poidsLettre > 50: #Sinon si poidsLettre est plus grands que 50
        prix = 1.10 #Redéfinir la valeur de prix

    print(f"Le prix de lettre est de {prix:0.2f}€")
except ValueError: #Si l'erreur capturé est de type ValueError, alors faire la suite
    print("Erreur !")