for _ in range(int(input())):
    n= int(input())
    coords=[tuple(map(int, input().split())) for _ in range(n)]
    s = [x +y for x, y in coords]
    print(2* (max(s)- min(s)))
