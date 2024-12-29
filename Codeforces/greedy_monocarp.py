# TODO : refaire
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    sum_coins = 0
    for x in a:
        if sum_coins + x <= k:
            sum_coins += x
        else:
            break

    print(k - sum_coins)
