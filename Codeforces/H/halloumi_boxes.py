import sys

data = sys.stdin.read().strip().split()

t,i = int(data[0]), 1

for _ in range(t):
    n, k = int(data[i]), int(data[i+1])
    i += 2
    a = list(map(int, data[i:i+n]))
    i += n

    if sorted(a) == a or k > 1:
        print("YES")
    else:
        print("NO")