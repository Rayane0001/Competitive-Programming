import sys

data = sys.stdin.read().strip().split()
t,i = int(data[0]), 1

for _ in range(t):
    s,i = int(data[i]), i +1
    n = 0
    while n*n < s:
        n += 1

    array = [str(x*x) for x in range(n)]

    sys.stdout.write(str(len(array)) + "\n")
