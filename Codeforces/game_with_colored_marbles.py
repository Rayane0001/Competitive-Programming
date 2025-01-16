from collections import Counter
for _ in range(int(input())):
    points = 0
    n = int(input())
    c = list(map(int,input().split()))
    c = [x - 1 for x in c]
    cnt = Counter(c)
    exactly1 = sum(1 for x in cnt.values() if x == 1)
    morethan1 = sum(1 for x in cnt.values() if x > 1)

    result = morethan1 + (exactly1 + 1) // 2 * 2
    print(result)
