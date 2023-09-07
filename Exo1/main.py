#Exercice 3
a = int(input("Saisissez un premier nombre"))
b = int(input("Saisissez un deuxième nombre"))
print(a + b)

#Exercice 3 extra
try:    
    a = int(input("Saisissez un premier nombre"))
    b = int(input("Saisissez un deuxième nombre"))
except ValueError:
    print("ERREUR !")