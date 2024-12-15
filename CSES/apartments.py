n, m, k = map(int, input().split())
desired_size = list(map(int, input().split()))
size = list(map(int, input().split()))

desired_size.sort()
size.sort()

a = 0
i = j = 0

while i < n and j < m:
    if abs(desired_size[i] - size[j]) <= k:
        a += 1
        i += 1
        j += 1
    elif desired_size[i] < size[j] - k:
        i += 1
    else:
        j += 1
print(a)