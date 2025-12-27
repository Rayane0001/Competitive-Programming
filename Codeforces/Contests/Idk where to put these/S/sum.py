t = int(input())

for _ in range(t):
    a,b,c = map(int,input().split())
    if a+c ==b or a+b ==c or c+b == a:
        print("YES")
    else:
        print("NO")