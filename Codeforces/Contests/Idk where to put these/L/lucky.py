for _ in range(int(input())):
    number = input().strip()

    if sum(int(number[i]) for i in range(3)) == sum(int(number[i]) for i in range(3, 6)):
        print("YES")
    else:
        print("NO")