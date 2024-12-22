from bisect import bisect_left, bisect_right

t = int(input())

for _ in range(t):
    # n : nb chiffres
    # x : borne inférieure pour la somme
    # y : borne supérieure pour la somme
    n, x, y = map(int, input().split())

    # a : séquence de nombres
    a = list(map(int, input().split()))

    total_sum = sum(a)
    interesting_numbers = 0

    freq = {}

    for num in a:
        freq[num] = freq.get(num, 0) + 1

    a.sort()

    for i in range(n):
        min_val = total_sum - y - a[i]
        max_val = total_sum - x - a[i]

        left = bisect_left(a, min_val, i + 1)
        right = bisect_right(a, max_val, i + 1)

        interesting_numbers += (right - left)

    print(interesting_numbers)
