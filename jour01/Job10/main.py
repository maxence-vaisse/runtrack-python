montant_investissement = 10000
taux = 1.15

print (montant_investissement * taux - montant_investissement)

montant_investissement += 5000
taux += 0.02

print (montant_investissement * taux - montant_investissement)

montant_investissement *= 0.9
taux -= 0.01

print (montant_investissement * taux - montant_investissement)

print("Le montant final de l'investissement est de ",montant_investissement,"")
print("Et le gain final en fonction du taux de rendement est de ",montant_investissement * taux - montant_investissement,"")