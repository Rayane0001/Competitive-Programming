# tags: greedy, implementation
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    while a and a[-1] == 0:
        a.pop()

    a.reverse()
    while a and a[-1] == 0:
        a.pop()
    a.reverse()

    if not a:
        print(0)
        continue

    has_zero = any(x == 0 for x in a)
    if has_zero:
        print(2)
    else:
        print(1)
