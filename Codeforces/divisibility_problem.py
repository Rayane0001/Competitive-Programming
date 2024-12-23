# tags: math
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    remainder = a % b
    if remainder == 0:
        print(0)
    else:
        print(b - remainder)