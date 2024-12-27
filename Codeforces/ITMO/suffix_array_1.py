s = input().strip()
n = len(s)
s += "$"

p = list(range(n + 1))
c = [ord(ch) for ch in s]

k = 0
while (1 << k) < n + 1:
    p.sort(key=lambda x: (c[x], c[(x + (1 << k)) % (n + 1)]))

    c_new = [0] * (n + 1)
    for i in range(1, n + 1):
        prev = (c[p[i - 1]], c[(p[i - 1] + (1 << k)) % (n + 1)])
        curr = (c[p[i]], c[(p[i] + (1 << k)) % (n + 1)])
        if curr > prev:
            c_new[p[i]] = c_new[p[i - 1]] + 1
        else:
            c_new[p[i]] = c_new[p[i - 1]]
    c = c_new
    k += 1

print(" ".join(map(str, p)))
