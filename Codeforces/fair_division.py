from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    t = Counter(a)
    nb1 = t[1]
    nb2 = t[2]

    total = nb1 + nb2 * 2
    if total % 2 != 0:
        print("NO")
    else:
        half = total // 2
        if half % 2 == 0 or (half% 2 == 1 and nb1>0):
            print("YES")
        else:
            print("NO")