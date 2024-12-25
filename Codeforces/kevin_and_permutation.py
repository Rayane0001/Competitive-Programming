# tags: permutation, math
for _ in range(int(input())):
    n, k = map(int, input().split())
    p = [0] * n
    for i in range(n // k):
        p[(i + 1) * k - 1] = i + 1
        x = n
    for i in range(n):
        if p[i] == 0:
            p[i] = x
            x -= 1
    print(*p)
