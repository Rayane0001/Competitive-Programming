import sys
import math
data = sys.stdin.read().split()
t, i = int(data[0]), 1
res = []
for _ in range(t):
    a,b,i = int(data[i]), int(data[i + 1]), i +2
    res.append(str(math.lcm(a,b)))
print("\n".join(res))
