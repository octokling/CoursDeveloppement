#Exercice 3 de moodle
#Dans cette exercice il faut que l'utilisateur entre 2 nombres et afficher un résultat en additionnant les deux nombre choisi par l'utilisateur

#Dans notre logique, nous avons fait cela :
a = input("Saisissez un premier nombre") #User output : 2
b = input("Saisissez un deuxième nombre") #User output : 10
print(a + b) #Print output: 210
#Nous voyons que le résultat n'était pas celui attendu, les chiffres se sont mit à la suite.
#Car les variables a et b sont de type str, et qu'en additionnant les variable de ce type, cela va juste les coller à la suite.
#Alors il faut convertir str en int, pour cela, python à un méthode de convertion simple

#La fonction int(), cette fonction convertir ce qu'il y a à l'interieur des () dans son type.
#Exemple : int(input()). Nous pouvons aussi le faire comme cela : int(a)

a = int(input("Saisissez un premier nombre")) #User output : 5
b = int(input("Saisissez un deuxième nombre")) #User output : 3
print(a + b) #Print output: 8
#Les deux variable ont enfin afficher le résultat attendu

#Exercice 3 extra
try:    
    a = int(input("Saisissez un premier nombre"))
    b = int(input("Saisissez un deuxième nombre"))

    print(a + b)
except ValueError:
    print("ERREUR !")
#Selon vous à quoi ce code ?