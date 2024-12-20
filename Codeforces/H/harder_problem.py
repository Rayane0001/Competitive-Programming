# WRONG ANSWER
t = int(input())
resultat = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    freq = [0] * (n + 1)
    max_f = 0
    for i in range(n):
        b.append(a[i])
        freq[a[i]] += 1
        max_f = max(max_f, freq[a[i]])
        if freq[a[i]] < max_f:
            for j in range(1, n + 1):
                if freq[j] == max_f:
                    b[-1] = j
                    freq[a[i]] -= 1
                    freq[j] += 1
                    break
    resultat.append(" ".join(map(str, b)))
print("\n".join(resultat))
