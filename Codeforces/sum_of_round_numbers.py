t = int(input())
for i in range(1, t + 1):
    n = int(input())
    ans = []
    power = 1
    while n > 0:
        if n % 10 > 0:
            ans.append((n % 10) * power)
        n //= 10
        power *= 10
    ans.sort(reverse=True)
    print(len(ans))
    print(*ans)
