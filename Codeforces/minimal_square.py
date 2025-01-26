for _ in range(int(input())):
    a, b = map(int, input().split())

    side1 = max(2* a, b)
    side2 = max(a, 2 * b)
    side_length = min(side1, side2)
    area = side_length ** 2
    print(area)