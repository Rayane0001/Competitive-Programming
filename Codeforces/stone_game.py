import sys

data = sys.stdin.read().strip().split()
t, i = int(data[0]), 1

for _ in range(t):
    n = int(data[i])
    stones = list(map(int, data[i + 1:i + 1 + n]))
    i += n + 1

    max_pos = stones.index(max(stones))
    min_pos = stones.index(min(stones))

    res = min(
        max(max_pos, min_pos) + 1,
        n - min(max_pos, min_pos),
        (n - max_pos) + (min_pos + 1),
        (n - min_pos) + (max_pos + 1)
    )

    sys.stdout.write(f"{res}\n")
