n = int(input())

points = list(map(int, input().split()))

amazing = 0

for i in range(1, n):
    if points[i] < min(points[:i]) or points[i] > max(points[:i]):
        amazing += 1

print(amazing)