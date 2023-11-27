L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

def produit_25_90(L, min_val, max_val):
    produit = 1
    for i in L:
        if min_val <= i <= max_val:
            produit *= i
    return produit

total = produit_25_90(L, 25, 90)
print(f" Le résultat des produits des nombres de la liste compris entre 25 et 90 est {total}")