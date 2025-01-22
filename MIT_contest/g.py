for _ in range(int(input())):
    n,m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    even= 0
    old =0

    for i in range(n):
        for j in range(m):
            if (i+ j) % 2 == 0:
                even+= grid[i][j]
            else:
                old += grid[i][j]

    if even %2 == old % 2:
        print("NO")
    else:
        print("YES")
