# tags: brute force, greedy, implementation, math, number theory
for _ in range(int(input())):
    n, k = map(int, input().split())  # Read n and k
    p = [0] * n  # Initialize permutation with zeros

    # Place the smallest numbers at multiples of k
    for i in range(n // k):
        p[(i + 1) * k - 1] = i + 1  # Assign smallest unused number to the position

    x = n  # Start filling from the largest number
    for i in range(n):
        if p[i] == 0:  # If position is not filled yet
            p[i] = x  # Assign the largest unused number
            x -= 1  # Decrease the number for next

    print(*p)  # Print the permutation

