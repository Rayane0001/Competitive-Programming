import sys
data = sys.stdin.read().split()
t, i = int(data[0]), 1
res = []

for _ in range(t):
    n, i = int(data[i]), i + 1
    res.append(str((n-3) // 3 -1))
print("\n".join(res))