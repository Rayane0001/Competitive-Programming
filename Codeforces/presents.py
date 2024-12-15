n = int(input())
gift = list(map(int, input().split()))
result = [0] * n

for i in range(n):
    result[gift[i] - 1] = i + 1

print(" ".join(map(str, result)))