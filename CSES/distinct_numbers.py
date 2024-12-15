n = int(input())
line = list(map(int, input().split()))

distinct_count = len(set(line))

print(distinct_count)