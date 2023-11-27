L = [8,24,48,2,16]

def multiples_3(list):
    multiple = 0
    for i in list:
        if i % 3 == 0:
            multiple += 1
    return multiple

print("Nombre de multiples de 3 dans la liste :", multiples_3(L))

# Autre méthode

# L = [8, 24,48,2,16]

# count = len([i for i in L if (i % 3 ==0)])

# print (count)