s = input().strip()  # On lit une chaîne sans espaces autour
n = len(s)           # Taille de la chaîne sans le caractère spécial ajouté
s += "$"             # On ajoute un caractère spécial '$' à la fin pour marquer la fin de la chaîne

# Initialisation des structures principales
p = list(range(n + 1))  # Positions des suffixes, initialement [0, 1, 2, ..., n]
c = [ord(ch) for ch in s]  # Classes d'équivalence initiales basées sur le code ASCII des caractères

# Étape 0 : longueur des segments = 1 caractère
k = 0  # Exposant qui détermine la longueur des segments (2^k)

# Boucle principale : On continue jusqu'à ce que les segments couvrent toute la chaîne
while (1 << k) < n + 1:  # Tant que la longueur des segments (2^k) est inférieure ou égale à la longueur totale de la chaîne

    # Tri des positions des suffixes en fonction des classes d'équivalence
    p.sort(key=lambda x: (c[x], c[(x + (1 << k)) % (n + 1)]))
    # Chaque suffixe est trié par une clé : (classe actuelle, classe de la "moitié suivante" du suffixe)

    # Mise à jour des classes d'équivalence
    c_new = [0] * (n + 1)  # Nouveau tableau pour les classes d'équivalence
    for i in range(1, n + 1):  # On compare chaque suffixe avec le précédent dans l'ordre trié
        prev = (c[p[i - 1]], c[(p[i - 1] + (1 << k)) % (n + 1)])
        curr = (c[p[i]], c[(p[i] + (1 << k)) % (n + 1)])
        # Si la clé actuelle est différente de la précédente, on augmente la classe
        if curr > prev:
            c_new[p[i]] = c_new[p[i - 1]] + 1
        else:  # Sinon, on garde la même classe
            c_new[p[i]] = c_new[p[i - 1]]
    c = c_new  # On met à jour les classes d'équivalence
    k += 1  # On passe à la longueur de segment suivante (2^(k+1))

# Résultat final : les positions triées des suffixes
print(" ".join(map(str, p)))  # On affiche les positions triées séparées par des espaces
