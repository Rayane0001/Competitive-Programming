# tags: implementation

n = int(input())
capacity = 0
max_capacity = 0
for _ in range(n):
    a, b = map(int, input().split())
    capacity -= a
    capacity += b
    if capacity > max_capacity:
        max_capacity = capacity

print(max_capacity)