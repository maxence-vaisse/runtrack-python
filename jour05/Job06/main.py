def distance_parcourue(nombre_marches, hauteur_marche):

    hauteur_marche_m = hauteur_marche / 100

    distance_aller_retour = 2 * nombre_marches * hauteur_marche_m

    distance_par_jour = 5 * distance_aller_retour

    distance_par_semaine = 7 * distance_par_jour

    return distance_par_semaine

nombre_marches = 100
hauteur_marche = 20
distance = distance_parcourue(nombre_marches, hauteur_marche)
print(f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance:.2f} m par semaine.")