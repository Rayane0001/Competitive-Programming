n = int(input())
t = list(map(int, input().split()))

groups = {1: [], 2:[], 3:[]}

for i, val in enumerate(t):
    groups[val].append(i+1)

nb_teams = min(len(groups[1]), len(groups[2]), len(groups[3]))

print(nb_teams)

for i in range(nb_teams):
    print(groups[1][i], groups[2][i], groups[3][i])