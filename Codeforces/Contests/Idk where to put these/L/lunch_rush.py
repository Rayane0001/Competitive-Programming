n,k = map(int, input().split())
max_joy = -float('inf')

for _ in range(n):
    f,t=map(int, input().split())

    joy = 0

    if t > k:
        joy = f - (t-k)
    else:
        joy = f

    max_joy = max(max_joy, joy)

print(max_joy)