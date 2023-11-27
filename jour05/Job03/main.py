def dessin_triangle(hauteur):
    for i in range(hauteur):
        if i == 0:
            ligne = ' ' * (hauteur - i) + '/' + '\\'
        elif i == hauteur - 1:
            ligne = ' /' + '_' * (2 * hauteur-2) + '\\'
        else:
            espaces = ' ' * (hauteur - i)
            ligne = espaces + '/' + ' ' * (2 * i) + '\\' + espaces
        print(ligne)

dessin_triangle(5)