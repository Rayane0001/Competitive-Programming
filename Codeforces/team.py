# tags: brute force, greedy

n = int(input())
nb_solutions = 0

for _ in range(n):
    if sum(map(int, input().split())) >= 2:
        nb_solutions += 1

print(nb_solutions)