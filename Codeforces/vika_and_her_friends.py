import sys

data = sys.stdin.read().strip().split()
t, i = int(data[0]), 1
res = []
for _ in range(t):
    n, m, k, i = int(data[i]), int(data[i + 1]), int(data[i + 2]), i + 3
    x, y, i = int(data[i]), int(data[i + 1]), i + 2
    ans = "YES"

    for _ in range(k):
        xx, yy, i = int(data[i]), int(data[i+1]), i+2
        if (x+y) % 2 == (xx+yy) % 2:
            ans = "NO"

    res.append(ans)

sys.stdout.write("\n".join(res) + "\n")