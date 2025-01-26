n = int(input())

x = list(map(int, input().split()))

sereja = 0
dima = 0

while x:
    if x[0] > x[-1]:
        sereja += x.pop(0)
    else:
        sereja += x.pop()

    if x:
        if x[0] > x[-1]:
            dima += x.pop(0)
        else:
            dima += x.pop()
    else:
        break

print(sereja, dima)