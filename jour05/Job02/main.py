def draw_rectangle(largeur, hauteur):
        hauteur_rectangle = 0
        print ("|" + "-" * largeur + "|")
        while hauteur_rectangle < hauteur - 2:
            print ("|" + " " * largeur + "|")
            hauteur_rectangle += 1
        print ("|" + "-" * largeur + "|")
        
draw_rectangle (10, 3)
