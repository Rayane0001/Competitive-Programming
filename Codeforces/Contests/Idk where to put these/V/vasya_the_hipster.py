a = list(map(int, input().split()))
a.sort()

diff_socks = a[0]
same_socks = max((a[1] - a[0]) // 2, 0)

print(diff_socks, same_socks)