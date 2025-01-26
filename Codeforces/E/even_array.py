for _ in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))

    odd_mismatch = sum(1 for i in range(n) if i%2 == 1 and array[i] % 2 == 0)
    even_mismatch = sum(1 for i in range(n) if i%2 == 0 and array[i] % 2 == 1)
    print(odd_mismatch if odd_mismatch == even_mismatch else -1)