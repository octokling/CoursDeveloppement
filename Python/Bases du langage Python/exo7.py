#Écrire le programme qui détermine le nombre de billets de 50 €, 20 € et 10 € que doit fournir un distributeur automatique en fonction d’une somme saisie sur un clavier.
#Remarque : les sommes saisies doivent toujours être des multiples de 10. Pour s’en assurer, contrôler et faire ressaisir l'utilisateur pour obtenir une somme demandée multiple de 10.
#Indication : Concevoir une fonction d’analyse de réponse.

argentVoulantEtreRetirer = int(input("Combien voulez-vous retirer ?")) #Déclare un input

if (argentVoulantEtreRetirer % 10) == 0 : #Le pourcentage se nomme "Modulo", c'est le résultat du reste d'un division
    #Si dans notre cas le le reste est égale à 0, alors nous pouvons dire que argentVoulantEtreRetirer est un multiple de 10
    CanGiveMoney = True #Cette variable boolean servira pour le while
    BilletDe50 = 0 #Ces variables servent à compter le nombre de billets distribué
    BilletDe20 = 0
    BilletDe10 = 0

    while(CanGiveMoney):#Ceci est un boucle, elle s'effectura à l'infini tant que CanGiveMoney soit égale à True
        if argentVoulantEtreRetirer >= 50: #Si argentVoulantEtreRetirer est supérieur ou égale à 50
            BilletDe50 = BilletDe50 + 1 #Ajoute d'un au compteur
            argentVoulantEtreRetirer = argentVoulantEtreRetirer - 50 #Enlève 50 au à la variable argentVoulantEtreRetirer
        elif argentVoulantEtreRetirer >= 20: #Si argentVoulantEtreRetirer est supérieur ou égale à 20
            BilletDe20 = BilletDe20 + 1#Ajoute d'un au compteur
            argentVoulantEtreRetirer = argentVoulantEtreRetirer - 20 #Enlève 20 au à la variable argentVoulantEtreRetirer
        elif argentVoulantEtreRetirer >= 10: #Si argentVoulantEtreRetirer est supérieur ou égale à 10
            BilletDe10 = BilletDe10 + 1#Ajoute d'un au compteur
            argentVoulantEtreRetirer = argentVoulantEtreRetirer - 10 #Enlève 10 au à la variable argentVoulantEtreRetirer
        else:
            CanGiveMoney = False #Lorsque ces conditions sont tous à False, CanGiveMoney est égale à False
    print(f"Je vous ai distribué {BilletDe10} billet(s) de 10€, {BilletDe20} billet(s) de 20€, {BilletDe50} billet(s) de 50€") #Affichage du nombre de billets distribué
else:
    print("Je ne peux pas donner la somme exacte d'argent que vous avez demandé.") #Lorsque argentVoulantEtreRetirer n'est pas un multiple de 10