def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note >= 40:
            multiple_suivant = ((note // 5) + 1) * 5
            if multiple_suivant - note < 3:
                notes_arrondies.append(multiple_suivant)
            else:
                notes_arrondies.append(note)
        else:
            notes_arrondies.append(note)
    return notes_arrondies

notes = [33, 38, 83, 82, 45]
notes_arrondies = arrondir_notes(notes)
print(notes_arrondies)

def arrondir_notes(liste_notes):
    notes_arrondies = []
    for note in liste_notes:
        if note >= 40 and note % 5 >= 3:
            note_arrondie = note + (5 - note % 5)
            notes_arrondies.append(note_arrondie)
        else:
            notes_arrondies.append(note)
    return notes_arrondies

liste_notes = [33, 38, 83, 82, 45]
notes_arrondies = arrondir_notes(liste_notes)
print("Notes originales :", liste_notes)
print("Notes arrondies :", notes_arrondies)