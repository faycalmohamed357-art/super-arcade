import random

secret = random.randint(1, 10)
trouve = False
tentatives = 0

print("--- JEU DE DEVINETTE ---")

while not trouve:
    essai = int(input("Devine le nombre (1 à 10) : "))
    tentatives = tentatives + 1  # On ajoute 1 à chaque essai
    
    if essai < secret:
        print("C'est PLUS grand !")
    elif essai > secret:
        print("C'est PLUS petit !")
    else:
        print("BRAVO ! Tu as trouvé en", tentatives, "coup(s) !")
        trouve = True

