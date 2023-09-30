# La définition d'une année bissextile est décrite ci-dessous (source wikipédia)

# 1. Si l'année est divisible par 4, passez à l'étape 2, sinon passez à l'étape 5. 

# 2. Si l'année est divisible par 100, passez à l'étape 3. Sinon, passez à l'étape 4

# 3. Si l'année est divisible par 400, passez à l'étape 4. Sinon, passez à l'étape 5. 

# 4. L'année est une année bissextile (elle a 366 jours). 

# 5. L'année n'est pas une année bissextile (elle a 365 jours). 

try:
    annee = int(input("Entrez une année : "))

    if annee % 4 == 0: #% = modulo, le reste d'un division posé
        if annee % 100 == 0:
            if annee % 400 == 0:
                print("L'année est une année bissextile (elle a 366 jours).")
            else: 
                print("L'année n'est pas une année bissextile (elle a 365 jours).")
        else: 
            print("L'année est une année bissextile (elle a 366 jours).")
    else:
        print("L'année n'est pas une année bissextile (elle a 365 jours).")

    
except ValueError:
    print("Erreur de valeur")