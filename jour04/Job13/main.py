ma_liste = [10,20,30,20,10,50,60,40,80,50,40]

liste_sans_doublon = []

for i in ma_liste:
    if i not in liste_sans_doublon:
        liste_sans_doublon += [i]

my_list = liste_sans_doublon

print("liste après supression des doublons", ma_liste)