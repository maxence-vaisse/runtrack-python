def nb_caractère(chaine):
    compteur = 0
    for caractere in chaine:
        compteur += 1
    return compteur

def my_long_word(longueur, phrase):
    mots_long = ""
    mots = phrase.split(" ")
    for mot in mots:
        if nb_caractère(mot) > longueur:
            if mots_long:
                mots_long += " "
            mots_long += mot
    return mots_long

joie_de_vivre = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
print(my_long_word(3, joie_de_vivre))