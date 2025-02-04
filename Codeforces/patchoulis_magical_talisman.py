import sys

data = sys.stdin.read().split()
t = int(data[0])
i = 1
res = []

for _ in range(t):
    n = int(data[i])
    i += 1
    arr = list(map(int, data[i:i + n]))
    i += n

    exponents = []
    for x in arr:
        cnt = 0
        while x % 2 == 0:
            cnt += 1
            x //= 2
        exponents.append(cnt)

    m = min(exponents)
    count_even = sum(1 for exp_val in exponents if exp_val > 0)

    answer = max(m - 1, 0) + count_even
    res.append(str(answer))

sys.stdout.write("\n".join(res))
