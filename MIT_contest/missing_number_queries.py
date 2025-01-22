n, q = map(int, input().split())
a = list(map(int, input().split()))
missings = {i for i in range(1, n + 1) if i not in a}

for _ in range(q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x, y = q[1] - 1, q[2]
        if a[x] in missings:
            missings.remove(a[x])
        a[x] = y
        if y not in a:
            missings.add(y)
    else:
        l, r = q[1] - 1, q[2]
        sub = set(a[l:r])
        for m in sorted(missings):
            if m not in sub:
                print(m)
                break
