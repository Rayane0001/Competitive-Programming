for _ in range(int(input())):
    n = int(input())

    nb_two = n // 3
    nb_one = n // 3
    rest = n % 3

    if rest == 1:
        nb_one += 1
    elif rest == 2:
        nb_two += 1

    print(nb_one, nb_two)