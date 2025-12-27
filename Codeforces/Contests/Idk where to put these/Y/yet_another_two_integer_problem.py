for _ in range(int(input())):
    a, b = map(int, input().split())
    diff = abs(a - b)
    moves = (diff + 9) // 10
    print(moves)
