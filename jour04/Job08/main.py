L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

def pairs(L):
    count = sum(i for i in L if i % 2 == 0)
    return count

print(f" la somme de tous les éléments pairs est {pairs(L)}")