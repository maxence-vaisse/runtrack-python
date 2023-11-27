# Liste donnée
L = [10, 8, 9, 12, 15, 17, 13]

# Fonction pour calculer la longueur de la liste sans utiliser la fonction système len()
def longueur(liste):
    compteur = 0
    for nombre in liste:
        compteur += 1
    return compteur

# Fonction pour trier la liste dans l'ordre croissant sans utiliser une fonction système
def trier(liste):
    echange = True
    while echange:
        echange = False
        index = 1 #démarre au deuxième élement pour toujours avoir un élément de comparaison
        while index < longueur(liste):
            if liste[index-1] > liste[index]:
                liste[index-1], liste[index] = liste[index], liste[index-1]
                echange = True
            index += 1
    return liste

print(trier(L))