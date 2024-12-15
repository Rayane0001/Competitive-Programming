# tags: implementation, strings

line1 = input().strip().lower()
line2 = input().strip().lower()

if line1 < line2:
    print(-1)

if line1 > line2:
    print("1")

if line1 == line2:
    print(0)