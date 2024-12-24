t = int(input())  # number of test cases
odd_digits = [1, 3, 5, 7, 9]

for _ in range(t):
    # n is the number of times we write d
    # d is the digit we are treating
    n, d = map(int, input().split())
    # so now ddd is n times d, which can be a huge number
    ddd = int(str(d) * n)  # this creates the number with n repetitions of d
    divisible_digits = []
    # check divisibility for each odd digit
    for digit in odd_digits:
        # if it can be divided by ddd
        if ddd % digit == 0:
            divisible_digits.append(str(digit))

    # print the divisible digits
    print(" ".join(divisible_digits))
    # ( this ain't printing the right thing idk why lol)
