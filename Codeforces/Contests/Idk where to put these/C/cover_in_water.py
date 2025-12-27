import sys

data = sys.stdin.read().split()

t = int(data[0])
i = 1

for _ in range(t):
    n = int(data[i])
    i += 1
    s = data[i]
    i += 1

    if "..." in s:
        res = 2
    else:
        res = s.count(".")

    print(f"{res}")
