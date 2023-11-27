L= [10, 20, 30, 40, 50]
def list(liste):
    return liste
print(list(L))

def list(liste):
    return liste[1]
print(list(L))

def list(liste):
    liste[3] = liste[2] + liste[4]
    return liste
print (list(L))

def list(liste):
    liste[3] = liste[2] + liste[4]
    return liste[-1]
print (list(L))