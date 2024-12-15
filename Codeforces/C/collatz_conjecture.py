# tags: brute force, implementation, math, number theory

# TODO : à refaire (1200)
t = int(input().strip())
results = []

for _ in range(t):
    x, y, k = map(int, input().strip().split())

    while k > 0 and x != 1:
        ost = ((x // y + 1) * y) - x
        ost = max(1, ost)
        ost = min(ost, k)

        x += ost
        while x % y == 0:
            x //= y
        k -= ost

    results.append(x + k % (y - 1))

for result in results:
    print(result)