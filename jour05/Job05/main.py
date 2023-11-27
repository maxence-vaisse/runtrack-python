def chiffrement_cesar(message, decalage):
    resultat = ""

    for caractere in message:
        # Vérifier si le caractère est une lettre
        if caractere.isalpha():
            # Déterminer la casse (majuscule ou minuscule)
            casse = ord('A') if caractere.isupper() else ord('a')

            # Appliquer le décalage en prenant en compte le dépassement
            caractere_decale = chr((ord(caractere) - casse + decalage) % 26 + casse)

            # Ajouter le caractère décalé au résultat
            resultat += caractere_decale
        else:
            # Si le caractère n'est pas une lettre, le laisser inchangé
            resultat += caractere

    return resultat

# Exemple d'utilisation
message_original = "Bonjour , je m'apelle Maxence Vaisse"
decalage = 3
message_decale = chiffrement_cesar(message_original, decalage)

print(f"Message original: {message_original}")
print(f"Message décalé: {message_decale}")
