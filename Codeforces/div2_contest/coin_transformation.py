def max_coins(n):
    if n<=3:
        return 1
    return 2* max_coins(n//4)

t = int(input())

for _ in range(t):
    n =int(input())
    print(max_coins(n))
