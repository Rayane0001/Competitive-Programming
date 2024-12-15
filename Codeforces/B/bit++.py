# tags: implementation

x = 0
statements = int(input())

for _ in range(statements):
    statement = input().strip()
    if "++" in statement:
        x += 1
    elif "--" in statement:
        x -= 1

print(x)