def my_sort(arr):
    """
    Trie une liste en utilisant l'algorithme de tri à bulles.

    Args:
    arr (list): La liste à trier.

    Returns:
    list: La liste triée.
    """
    n = len(arr)  # Longueur de la liste
    coups = 0  # Initialisation du nombre de coups nécessaires

    # Parcourir la liste
    for i in range(n):
        # Le dernier i éléments sont déjà triés, donc on réduit la boucle interne
        for j in range(0, n-i-1):
            # Comparer les éléments adjacents
            if arr[j] > arr[j+1]:
                # Échanger les éléments
                arr[j], arr[j+1] = arr[j+1], arr[j]
                coups += 1  # Incrémenter le nombre de coups

    # Afficher le nombre total de coups nécessaires
    print(f"Nombre total de coups nécessaires : {coups}")

    return arr

# Exemple d'utilisation
ma_liste = [64, 34, 25, 12, 22, 11, 90]
resultat = my_sort(ma_liste)
print("Liste triée:", resultat)
