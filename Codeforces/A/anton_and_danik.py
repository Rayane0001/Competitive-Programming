# tags: implementation, strings

from collections import Counter

n = int(input())
s = input().strip()

counter = Counter(s)

if counter['A'] > counter['D']:
    print("Anton")
elif counter['D'] > counter['A']:
    print("Danik")
elif counter['D'] == counter['A']:
    print("Friendship")