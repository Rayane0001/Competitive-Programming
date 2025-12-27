# tags: greedy, math

t = int(input())
for _ in range(t):
    m, a, b, c = map(int, input().split())
    row1 = min(a, m)
    row2 = min(b, m)
    rem_row1 = m - row1
    rem_row2 = m - row2
    no_pref = min(c, rem_row1 + rem_row2)
    total_seats = row1 + row2 + no_pref
    print(total_seats)