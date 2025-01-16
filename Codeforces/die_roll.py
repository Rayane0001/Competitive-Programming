from math import gcd

y, w = map(int, input().split())
max_roll = max(y, w)
favorable = 7 - max_roll
g = gcd(favorable, 6)
print(f"{favorable // g}/{6 // g}")
