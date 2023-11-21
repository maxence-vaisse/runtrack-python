def est_nombre_premier(nombre):
    if nombre < 2:
        return False
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            return False
    return True

def afficher_nombres_premiers(maximum):
    for nombre in range(2, maximum + 1):
        if est_nombre_premier(nombre):
            print(nombre, end=" ")


afficher_nombres_premiers(1000)