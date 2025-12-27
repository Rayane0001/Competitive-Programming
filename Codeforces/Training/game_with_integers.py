import sys

data = sys.stdin.read().strip().split()

t,i = int(data[0]), 1

for _ in range(t):
    n,i = int(data[i]), i +1

    if n % 3 == 0:
        print("Second")
    else:
        print("First")