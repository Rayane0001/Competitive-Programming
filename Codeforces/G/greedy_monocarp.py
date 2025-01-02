# tags: greedy, sortings

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    sum_coins = 0
    for coins in a:
        if sum_coins + coins <= k:
            sum_coins += coins
        else:
            break

    print(k - sum_coins)