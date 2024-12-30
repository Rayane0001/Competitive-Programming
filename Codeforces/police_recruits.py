n = int(input())
events = map(int, input().split())

polices = 0
crimes = 0

for event in events:
    if event > 0:
        polices += event
    elif event == -1:
        if polices > 0:
            polices -= 1
        else:
            crimes += 1

print(crimes)
