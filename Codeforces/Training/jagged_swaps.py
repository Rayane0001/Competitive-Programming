import sys

data = sys.stdin.read().split()
t = int(data[0])
i = 1

for _ in range(t):
    n = int(data[i])
    i += 1
    arr = list(map(int, data[i:i + n]))
    i += n

    print("YES" if arr[0] == 1 else "NO")
