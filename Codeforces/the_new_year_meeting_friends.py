x1, x2, x3 = map(int, input().split())

max_distance = max(x1, x2, x3) - min(x1, x2, x3)

print(max_distance)