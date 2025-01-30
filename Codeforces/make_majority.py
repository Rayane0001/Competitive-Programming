import sys

data = sys.stdin.read().strip().split()
t, i = int(data[0]), 1
res = []

for _ in range(t):
    n, a, i = int(data[i]), data[i+1], i + 2
    ok = a.count("111") >= 1 or a.count("11") >= 2 or (a.count("11") >= 1 and (a[0] == "1" or a[-1] == "1")) or (a[0] == "1" and a[-1] == "1")
    res.append("Yes" if ok else "No")

sys.stdout.write("\n".join(res) + "\n")
