import sys

input = sys.stdin.read
data = input().split()
t = int(data[0])
i = 1

for _ in range(t):
    p = list(map(int, data[i:i + 3]))
    i += 3
    d = -1

    max_p01 = min(p[0], p[1])
    max_p02 = min(p[0], p[2])
    max_p12 = min(p[1], p[2])

    for p01 in range(max_p01 + 1):
        for p02 in range(max_p02 + 1):
            r0 = p[0] - p01 - p02
            if r0 < 0 or r0 % 2 != 0:
                continue

            for p12 in range(max_p12 + 1):
                r1 = p[1] - p01 - p12
                r2 = p[2] - p02 - p12

                if r1 < 0 or r2 < 0:
                    continue
                if r1 % 2 != 0 or r2 % 2 != 0:
                    continue

                d = max(d, p01 + p02 + p12)

    print(d)
