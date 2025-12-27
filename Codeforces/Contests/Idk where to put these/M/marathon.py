for _ in range(int(input())):
    a,b,c,d= map(int, input().split())
    front = sum(1 for x in [b, c, d] if x > a)
    print(front)

