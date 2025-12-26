import bisect
import sys

sys.setrecursionlimit(3 * 10**5)
n, m = map(int, input().split())
prices = sorted(list(map(int, input().split())))
parent = list(range(n + 1))

def getpar(u):
    if u < 0 or u == parent[u]:
        return u
    parent[u] = getpar(parent[u])
    return parent[u]

for customer in map(int, input().split()):
    idx = bisect.bisect(prices, customer) - 1
    available = getpar(idx)
    if available >= 0:
        print(prices[available])
        parent[available] -= 1
    else:
        print(-1)