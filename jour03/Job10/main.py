def pair_impair(n):
    if type(n) != int or n <= 0:  
        return "Veuillez entrer un entier positif et non nul."
    elif n % 2 == 0:
        return "pair"
    else:
        return "impair"

print(pair_impair(-3))  
print(pair_impair(0))   
print(pair_impair(3))   
print(pair_impair(12))  
print(pair_impair(13)) 
print(pair_impair(-12)) 