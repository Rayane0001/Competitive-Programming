for _ in range(int(input())):
    k = int(input())
    number = 0
    count = 0

    while count < k:
        number += 1
        if number % 3 != 0 and number % 10 != 3:
            count += 1

    print(number)
