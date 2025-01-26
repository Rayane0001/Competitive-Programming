pointM, pointC = 0, 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    pointM += a > b
    pointC += a < b

print("Mishka" if pointM > pointC else "Chris" if pointM < pointC else "Friendship is magic!^^")
