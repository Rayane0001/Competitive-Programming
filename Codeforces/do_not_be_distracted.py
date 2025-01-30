# TODO
import sys

data = sys.stdin.read().split()
t,i = int(data[0]), 1
result = []
for _ in range(t):
    n, s, i = data[i], data[i+1], i+2
    result.append("NO" if any(s[k] != c for c in set(s) for k in range(s.find(c), s.rfind(c)+1)) else "YES")
print("\n".join(result))