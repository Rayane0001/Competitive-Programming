# tags: implementation

n = int(input())

t = list(map(int, input().split()))

found = False

for i in range(n):
    if t[i] == 1:
        print("HARD")
        found = True
        break

if not found:
    print("EASY")