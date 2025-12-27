import sys
from collections import Counter

data = sys.stdin.read().strip().split()
t, i = int(data[0]), 1
res = []

for _ in range(t):
    n, i = int(data[i]), i + 1
    a, i = list(map(int, data[i:i + n])), i + n

    occ = Counter(a)

    if len(occ) >= 3:
        res.append("No")
    else:
        values = list(occ.values())

        if abs(values[0] - values[-1]) <= 1:
            res.append("Yes")
        else:
            res.append("No")
            
sys.stdout.write("\n".join(res) + "\n")