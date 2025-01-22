for _ in range(int(input())):
    s1, s2 = input().split()

    # Vérifie si les deux chaînes ont les mêmes caractères
    if s1.count('A') != s2.count('A') or s1.count('B') != s2.count('B'):
        print(-1)
        continue

    ab, ba = 0, 0

    # Comptabilise les déséquilibres
    for a, b in zip(s1, s2):
        if a == 'A' and b == 'B':
            ab += 1
        elif a == 'B' and b == 'A':
            ba += 1

    # Les swaps AB ↔ BA
    swaps = min(ab, ba)

    # Les déséquilibres restants nécessitent deux opérations chacun
    remaining = abs(ab - ba)
    print(swaps + remaining)
