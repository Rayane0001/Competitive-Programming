for _ in range(int(input())):
    n = int(input())

    if n % 4 != 0:
        print("NO")
    else:
        print("YES")
        even = [2 * i for i in range(1, n // 2 + 1)]
        odd = [2 * i - 1 for i in range(1, n // 2)]
        odd.append(n + n // 2 - 1)
        print(*even, *odd)
