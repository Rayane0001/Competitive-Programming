from collections import Counter

for _ in range(int(input())):
    n = int(input())
    elements = list(map(int, input().split()))

    count = Counter(elements)
    unique_element = [key for key, value in count.items() if value == 1][0]

    print(elements.index(unique_element) + 1)