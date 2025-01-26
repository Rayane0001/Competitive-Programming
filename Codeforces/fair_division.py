from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    t = Counter(a)
    total = t[1] + t[2] * 2
    print("YES" if total % 2 == 0 and (total // 2 % 2== 0 or t[1] > 0) else "NO")