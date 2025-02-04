from math import gcd

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(key=lambda x: x%2)
    good = 0
    for i in range(n):
        for j in range(i + 1, n):
            if gcd(a[i], 2*a[j]) > 1:
                good += 1

    print(good)
