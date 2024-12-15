n, h = map(int, input().split())
width = n
heights = list(map(int, input().split()))

for i in range(len(heights)):
    if heights[i] > h:
        width += 1

print(width)


