L= [10, 20, 30, 40, 50]
def list(liste):
    return liste
print(list(L))


def list(liste):
    liste[0], liste[-1] = liste[-1], liste[0]
    return liste
print(list(L))