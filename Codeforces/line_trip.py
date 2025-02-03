import sys

data = sys.stdin.read().strip().split()

t,i=int(data[0]), 1

for _ in range(t):
    n,x = int(data[i]), int(data[i+1])
    i += 2
    a = list(map(int, data[i:i+n]))
    i+=n

    prev = 0
    max_gap = 0

    for station in a:
        max_gap = max(max_gap, station - prev)
        prev = station

    max_gap = max(max_gap, 2 * (x - prev))

    print(f"{max_gap}")