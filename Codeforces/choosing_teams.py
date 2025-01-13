n, k = map(int, input().split())

year = list(map(int, input().split()))
year.sort()

eligible = [y for y in year if y + k <= 5]

nb_teams = len(eligible) // 3

print(nb_teams)
