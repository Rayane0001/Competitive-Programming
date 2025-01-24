for _ in range(int(input())):
    x,y,n=map(int,input().split())
    k=n-(n%x)+y
    if k>n:
        k-=x
    print(k)