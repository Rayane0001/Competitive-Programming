# tags : implementation, strings
n = int(input())
string = input().strip().lower()

if set('abcdefghijklmnopqrstuvwxyz').issubset(set(string)):
    print("YES")
else:
    print("NO")