import sys
from collections import defaultdict

sys.setrecursionlimit(3 * 10**5)

def solve():
    n = int(input())

    events = defaultdict(int)

    for _ in range(n):
        a, b = map(int, input().split())
        events[a] += 1
        events[b] -= 1

    sorted_times = sorted(events.keys())

    current_customers = 0
    max_customers = 0

    for time in sorted_times:
        current_customers += events[time]
        max_customers = max(max_customers, current_customers)

    print(max_customers)

solve()
