L = [7, 11, 42, 39, 2]
def list(liste):  
    for i in range(len(liste)):
        liste[i] += 1
    return liste

print(list(L)) 


# autre façon de faire 

L=[7, 11, 42, 39, 2]

def list_add1(liste):
    newlist=[i + 1 for i in liste]
    return newlist

L_add1 = list_add1(L)

print(L_add1)