from collections import Counter
for _ in range(int(input())):
    print(Counter(map(int, input().split())).most_common(2)[1][0])
