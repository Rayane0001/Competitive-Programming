from collections import Counter

guest = input().strip()
host = input().strip()
pile = input().strip()

if Counter(guest) + Counter(host) == Counter(pile):
    print("YES")
else:
    print("NO")
