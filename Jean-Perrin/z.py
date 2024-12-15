from collections import defaultdict

def find_largest_frequent_prefix():

    N = int(input().strip())
    words = [input().strip() for _ in range(N)]

    # Stockage des préfixes et de leur fréquence
    prefix_count = defaultdict(int)

    # Générer les préfixes
    for word in words:
        for i in range(1, len(word) + 1):
            prefix = word[:i]
            prefix_count[prefix] += 1

    # Trouver le préfixe ayant la plus grande fréquence et la plus grande longueur
    max_prefix, max_count = "", 0
    for prefix, count in prefix_count.items():
        # Si la fréquence est meilleure, ou si la longueur est meilleure à fréquence égale
        if count > max_count or (count == max_count and len(prefix) > len(max_prefix)):
            max_prefix, max_count = prefix, count

    print(max_prefix, max_count)

find_largest_frequent_prefix()
