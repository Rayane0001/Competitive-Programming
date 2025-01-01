n, k = map(int, input().split())

limit = 240 - k
time = 0
nb_problems = 0

for i in range(1, n + 1):
    time += 5 * i
    if time > limit:
        break
    nb_problems += 1

print(nb_problems)
