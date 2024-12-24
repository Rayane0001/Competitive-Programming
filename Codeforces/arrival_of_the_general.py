n = int(input())

sizes = list(map(int, input().split()))

max_pos = sizes.index(max(sizes))
min_pos = sizes[::-1].index(min(sizes))
min_pos = n-1 - min_pos

if max_pos > min_pos:
    seconds = max_pos + (n-1 -min_pos) -1
else:
    seconds = max_pos + (n-1 - min_pos)

print(seconds)