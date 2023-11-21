chaine_base = "abcdefghijklmnopqrstuvwxyz" * 10

longueur_ligne = 1

while longueur_ligne <= len(chaine_base):

    print(chaine_base[:longueur_ligne])

    longueur_ligne += 2

    if longueur_ligne > len(chaine_base):
        break