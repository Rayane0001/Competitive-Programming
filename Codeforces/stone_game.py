import sys

data = sys.stdin.read().strip().split()
t, i = int(data[0]), 1

for _ in range(t):
    n = int(data[i])
    stones = list(map(int, data[i + 1:i + 1 + n]))
    i += n + 1

    min_idx = stones.index(min(stones))
    max_idx = stones.index(max(stones))

    option1 = max(min_idx + 1, max_idx + 1)
    option2 = max(n - min_idx, n - max_idx)
    option3 = (min_idx + 1) + (n - max_idx)
    option4 = (max_idx + 1) + (n - min_idx)

    result = min(option1, option2, option3, option4)

    sys.stdout.write(f"{result}\n")
