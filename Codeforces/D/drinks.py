# tags: implementation, math

n = int(input())
p = list(map(int, input().split()))

average = sum(p) / n
print(f"{average:.12f}")