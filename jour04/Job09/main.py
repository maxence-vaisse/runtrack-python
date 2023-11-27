L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

def max_min(L):
    valeur_max = max(L)
    valeur_min = min(L)
    return (valeur_max, valeur_min)

resultat_max_min = max_min(L)

print(f"La valeur maximum est {resultat_max_min[0]}")
print(f"la valeur minimum est {resultat_max_min[1]}")


# Autres méthodes
# L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
# def max_min(L):
    # v_max=max(L)
    # v_min=min(L)
    # return (v_max, v_min)
# v_max=max(L)
# v_min=min(L)
# print(f"la valeur max est:{v_max}")
# print(f"la valeur max est:{v_min}")