import sys

data = list(map(int, sys.stdin.read().strip().split()))
t, i = data[0], 1

for _ in range(t):
    n = data[i]
    a = data[i + 1:i + 1 + n]
    i += n + 1

    # On cherche à maximiser f(a) + f(b).
    # f(x) --> moyenne de la sous-séquence x

    res = max(a)
    a.remove(res)

    res += sum(a) / len(a) if a else 0
    sys.stdout.write(f"{res:.9f}\n")
