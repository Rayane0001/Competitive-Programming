for _ in range(int(input())):
    n = int(input())

    if n % 2 != 0 or n<4:
        print("-1")
        continue

    min_bus = (n+5) // 6
    max_bus = n // 4

    print(min_bus, max_bus)