nom="Bonnet Lacoste"
prixU=55
stock=25


print('nom')

print("Le prix du ",nom," et de ",prixU,"€ et il y a un stock de ",stock," bonnets")

print("Ajout de 10 ",nom," au stock")
stock+=10

print("A bien était ajouté au stock")

print("Il ya maintenant un stock de ",stock," ",nom,"")

quantite_achetee = int(input("Combien de ",nom," voulez vous acheter ? "))

stock -= quantite_achetee
print(f"Vous avez acheté {quantite_achetee} unité(s) de {nom}.")

# Mise à jour du prix en raison de l'inflation (augmentation de 10%)
prixU *= 1.1
print("Actualisation stock après inflation",nom," ",stock," ",prixU," ")