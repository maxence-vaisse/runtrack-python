L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

def longueur(liste):
    compteur = 0
    for nombre in liste:
        compteur += 1
    return compteur

def arrondir_custom(liste):
    i = 0
    while i < longueur(liste):
        liste[i] = liste[i]// 1
        i += 1

def trier(liste):
    echange = True
    while echange:
        echange = False
        index = 1
        while index < longueur(liste):
            if liste[index-1] > liste[index]:
                liste[index-1], liste[index] = liste[index], liste[index-1]
                echange = True
            index += 1
    return liste

# Arrondir chaque élément de L
arrondir_custom(L)

# Trier la liste arrondie
L_triee = trier(L)

print(L_triee)